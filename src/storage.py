"""SQLite storage for URL mappings + click analytics."""
import os
import sqlite3
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any


DB_PATH = os.getenv("DATABASE_URL", "data/urls.db").replace("sqlite:///", "")


def _connect():
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    con = _connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            code TEXT PRIMARY KEY,
            original_url TEXT NOT NULL,
            created_at TEXT NOT NULL,
            clicks INTEGER NOT NULL DEFAULT 0
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            clicked_at TEXT NOT NULL,
            user_agent TEXT,
            referrer TEXT,
            FOREIGN KEY (code) REFERENCES urls(code)
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_clicks_code ON clicks(code)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_clicks_date ON clicks(clicked_at)")
    con.commit()
    con.close()


def now_iso():
    return datetime.utcnow().isoformat()


def save_url(code: str, original_url: str) -> bool:
    con = _connect()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO urls (code, original_url, created_at, clicks) VALUES (?, ?, ?, 0)",
            (code, original_url, now_iso())
        )
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        con.close()


def get_url(code: str) -> Optional[Dict[str, Any]]:
    con = _connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM urls WHERE code = ?", (code,))
    row = cur.fetchone()
    con.close()
    return dict(row) if row else None


def get_url_by_original(original_url: str) -> Optional[Dict[str, Any]]:
    con = _connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM urls WHERE original_url = ? LIMIT 1", (original_url,))
    row = cur.fetchone()
    con.close()
    return dict(row) if row else None


def record_click(code: str, user_agent: str = "", referrer: str = ""):
    con = _connect()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO clicks (code, clicked_at, user_agent, referrer) VALUES (?, ?, ?, ?)",
        (code, now_iso(), user_agent or "", referrer or "")
    )
    cur.execute("UPDATE urls SET clicks = clicks + 1 WHERE code = ?", (code,))
    con.commit()
    con.close()


def get_analytics(code: str) -> Optional[Dict[str, Any]]:
    url = get_url(code)
    if not url:
        return None

    con = _connect()
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) AS total FROM clicks WHERE code = ?", (code,))
    total_clicks = cur.fetchone()["total"]

    # Clicks in last 7 days
    week_ago = (datetime.utcnow() - timedelta(days=7)).isoformat()
    cur.execute(
        "SELECT COUNT(*) AS c FROM clicks WHERE code = ? AND clicked_at >= ?",
        (code, week_ago)
    )
    last_7_days = cur.fetchone()["c"]

    # Daily breakdown (last 7 days)
    cur.execute(
        """SELECT substr(clicked_at, 1, 10) AS day, COUNT(*) AS c
           FROM clicks WHERE code = ? AND clicked_at >= ?
           GROUP BY day ORDER BY day""",
        (code, week_ago)
    )
    daily = [dict(r) for r in cur.fetchall()]

    # Top referrers
    cur.execute(
        """SELECT COALESCE(referrer, '') AS referrer, COUNT(*) AS c
           FROM clicks WHERE code = ? AND referrer != ''
           GROUP BY referrer ORDER BY c DESC LIMIT 5""",
        (code,)
    )
    top_referrers = [dict(r) for r in cur.fetchall()]

    con.close()

    return {
        "code": code,
        "original_url": url["original_url"],
        "total_clicks": total_clicks,
        "clicks_last_7_days": last_7_days,
        "daily_breakdown": daily,
        "top_referrers": top_referrers,
        "created_at": url["created_at"],
    }


def list_urls(limit: int = 100) -> List[Dict[str, Any]]:
    con = _connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM urls ORDER BY created_at DESC LIMIT ?", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    con.close()
    return rows


def delete_url(code: str) -> bool:
    con = _connect()
    cur = con.cursor()
    cur.execute("DELETE FROM urls WHERE code = ?", (code,))
    con.execute("DELETE FROM clicks WHERE code = ?", (code,))
    con.commit()
    changed = cur.rowcount > 0
    con.close()
    return changed
