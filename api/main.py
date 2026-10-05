"""FastAPI URL Shortener service."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict, Any

from shortener import generate_short_code, is_valid_url, is_valid_code
from storage import (
    init_db, save_url, get_url, get_url_by_original,
    record_click, get_analytics, list_urls, delete_url
)
from ratelimit import limiter


BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


app = FastAPI(
    title="URL Shortener Service",
    description="Scalable URL shortener with caching, rate limiting, and click analytics",
    version="1.0.0",
)


# ---------- Models ----------
class ShortenRequest(BaseModel):
    url: str = Field(..., min_length=8, max_length=2048)
    custom_code: Optional[str] = Field(None, min_length=3, max_length=12)


class ShortenResponse(BaseModel):
    code: str
    short_url: str
    original_url: str
    created_at: str


class AnalyticsResponse(BaseModel):
    code: str
    original_url: str
    total_clicks: int
    clicks_last_7_days: int
    daily_breakdown: List[Dict[str, Any]]
    top_referrers: List[Dict[str, Any]]
    created_at: str


# ---------- Startup ----------
@app.on_event("startup")
def startup():
    init_db()
    print("[OK] Database initialized")


# ---------- Helpers ----------
def client_key(request: Request) -> str:
    return request.client.host if request.client else "unknown"


def check_rate(request: Request):
    allowed, remaining = limiter.allow(client_key(request))
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again in a minute."
        )


# ---------- Routes ----------
@app.get("/")
def root():
    return {"message": "URL Shortener Service", "docs": "/docs", "shorten": "POST /shorten"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/shorten", response_model=ShortenResponse)
def shorten(req: ShortenRequest, request: Request):
    check_rate(request)

    if not is_valid_url(req.url):
        raise HTTPException(status_code=400, detail="Invalid URL. Must start with http:// or https://")

    # Idempotent: return existing short code if URL already shortened
    existing = get_url_by_original(req.url)
    if existing:
        return ShortenResponse(
            code=existing["code"],
            short_url=f"{BASE_URL}/{existing['code']}",
            original_url=existing["original_url"],
            created_at=existing["created_at"],
        )

    # Custom code path
    if req.custom_code:
        if not is_valid_code(req.custom_code):
            raise HTTPException(status_code=400, detail="Custom code must be alphanumeric (max 12 chars)")
        if get_url(req.custom_code):
            raise HTTPException(status_code=409, detail="Custom code already in use")
        code = req.custom_code
    else:
        # Random with collision retry
        for _ in range(5):
            code = generate_short_code()
            if not get_url(code):
                break
        else:
            raise HTTPException(status_code=500, detail="Could not generate unique code")

    save_url(code, req.url)
    url = get_url(code)

    return ShortenResponse(
        code=code,
        short_url=f"{BASE_URL}/{code}",
        original_url=req.url,
        created_at=url["created_at"],
    )


@app.get("/{code}")
def redirect(code: str, request: Request):
    if not is_valid_code(code):
        raise HTTPException(status_code=404, detail="Not found")

    url = get_url(code)
    if not url:
        raise HTTPException(status_code=404, detail="Short code not found")

    record_click(
        code,
        user_agent=request.headers.get("user-agent", ""),
        referrer=request.headers.get("referer", ""),
    )

    return RedirectResponse(url=url["original_url"], status_code=307)


@app.get("/analytics/{code}", response_model=AnalyticsResponse)
def analytics(code: str):
    result = get_analytics(code)
    if not result:
        raise HTTPException(status_code=404, detail="Short code not found")
    return result


@app.get("/urls")
def urls(limit: int = 100):
    return list_urls(limit)


@app.delete("/urls/{code}")
def remove(code: str, x_admin: Optional[str] = Header(None)):
    # Simple admin gate: pass header X-Admin: your-secret
    if x_admin != os.getenv("ADMIN_TOKEN", "admin-secret"):
        raise HTTPException(status_code=403, detail="Admin token required")
    if not delete_url(code):
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": code}
