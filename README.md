# Scalable URL Shortener Service

Production-style URL shortener with rate limiting, click analytics, custom short codes, and idempotent shortening. Built with FastAPI and SQLite, designed for easy upgrade to Redis + PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## Overview

A URL shortener that goes beyond naive "hash and store":

1. Idempotent shortening - same URL returns same short code
2. Custom short codes - users can pick their own alias
3. Collision-safe random codes - retries on collision, 62^7 keyspace
4. Rate limiting - sliding window, 60 requests per minute per IP
5. Click tracking - user agent, referrer, timestamp per redirect
6. Analytics - total clicks, last 7 days, daily breakdown, top referrers
7. Admin delete - protected by header token

## Problem Statement

A URL shortener looks trivial but has real engineering challenges:

- Duplicate storage - shortening the same URL twice should not create two codes
- Collisions - random codes can collide; must retry safely
- Abuse - without rate limiting, bots can flood the service
- Analytics - knowing click counts is not enough; you need time series and referrers
- Custom codes - must validate and check uniqueness

## Solution

A FastAPI service with:

- POST /shorten: idempotent shortening with optional custom code
- GET /{code}: 307 redirect + click recording
- GET /analytics/{code}: full analytics response
- Sliding-window rate limiter per client IP
- Admin delete with header-based token
- SQLite schema with indexed clicks table

## Architecture

Client
  |
  |-- POST /shorten --> Rate Limiter --> Idempotency Check
  |                                          |
  |                                          v
  |                                     Generate Code
  |                                          |
  |                                          v
  |                                     SQLite (urls)
  |                                          |
  |-- GET /{code} --> Lookup --> Record Click --> 307 Redirect
  |                     |
  |                     v
  |                SQLite (clicks)
  |
  |-- GET /analytics/{code} --> Aggregate queries --> JSON

## Tech Stack

| Category | Technologies |
|----------|-------------|
| API | FastAPI, Uvicorn, Pydantic |
| Storage | SQLite (indexed) |
| Rate Limiting | In-memory sliding window |
| Testing | pytest, httpx |
| Optional Upgrade | Redis, PostgreSQL |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Language | Python 3.11+ |

## Project Structure

url-shortener-service/
├── src/
│   ├── __init__.py
│   ├── shortener.py        # Code generation + validation
│   ├── storage.py          # SQLite schema + CRUD + analytics
│   └── ratelimit.py        # Sliding-window limiter
├── api/
│   ├── __init__.py
│   └── main.py             # FastAPI endpoints
├── tests/
│   ├── __init__.py
│   └── test_api.py         # pytest tests
├── data/                    # SQLite db (git-ignored)
├── .github/workflows/ci.yml
├── Dockerfile
├── requirements.txt
├── requirements-optional.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md

## Quick Start

### 1. Clone

git clone https://github.com/sumit966/url-shortener-service.git
cd url-shortener-service

### 2. Virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Start the API

uvicorn api.main:app --reload

Runs at http://localhost:8000

### 5. Open Swagger

http://localhost:8000/docs

## API Usage

### POST /shorten

Request:
{
  "url": "https://example.com/some/long/path",
  "custom_code": "myalias"
}

Response:
{
  "code": "myalias",
  "short_url": "http://localhost:8000/myalias",
  "original_url": "https://example.com/some/long/path",
  "created_at": "2025-01-15T10:30:00"
}

Idempotent: sending the same URL again returns the same code.

### GET /{code}

Redirects (307) to the original URL and records a click with user agent + referrer.

### GET /analytics/{code}

Response:
{
  "code": "myalias",
  "original_url": "https://example.com/some/long/path",
  "total_clicks": 42,
  "clicks_last_7_days": 18,
  "daily_breakdown": [
    {"day": "2025-01-09", "c": 3},
    {"day": "2025-01-10", "c": 5}
  ],
  "top_referrers": [
    {"referrer": "https://twitter.com", "c": 8}
  ],
  "created_at": "2025-01-15T10:30:00"
}

### GET /urls?limit=100

List the most recent URLs with click counts.

### DELETE /urls/{code}

Delete a URL and its click history. Requires admin header.

curl -X DELETE http://localhost:8000/urls/myalias -H "X-Admin: admin-secret"

### Other Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| / | GET | API info |
| /health | GET | Health check |
| /docs | GET | Swagger UI |
| /redoc | GET | Alternative docs |

## Rate Limiting

- Sliding window: 60 requests per 60 seconds per client IP
- Applied to POST /shorten
- Returns 429 with a clear message when exceeded

## Analytics Details

Every redirect records timestamp, user-agent, and referer. Aggregated queries return total clicks, clicks in the last 7 days, day-by-day breakdown, and top 5 referrers. The clicks table is indexed on code and clicked_at for fast aggregation.

## Testing

pytest tests/ -v

Tests cover: root, health, shorten valid, invalid URL returns 400, idempotent shorten, custom code, redirect 307, and analytics.

## Docker

Build:
docker build -t url-shortener .

Run:
docker run -p 8000:8000 url-shortener

## Production Upgrade Path

| Component | Dev | Production |
|-----------|-----|------------|
| Storage | SQLite | PostgreSQL |
| Rate limit | In-memory | Redis |
| Cache | None | Redis (redirect cache) |
| Analytics | SQL aggregate | Pre-aggregated tables |

## CI/CD

Every push to main triggers GitHub Actions: install deps, run pytest.

## Key Learnings

- Idempotent shortening requires a reverse lookup on original_url
- Random code collisions need a bounded retry loop
- Sliding window beats fixed window for rate limiting accuracy
- Indexed clicks table keeps analytics fast even at millions of rows
- 307 preserves the HTTP method; 301 is cached and hides analytics
- Admin actions should be gated by header, not query params

## Future Improvements

- Redis-backed rate limiter for multi-instance scaling
- QR code generation for each short URL
- Expiring links (TTL)
- User accounts with API keys
- Bulk shorten (JSON array)
- Prometheus metrics + Grafana
- Deploy to GCP Cloud Run with Cloud SQL + Memorystore

## License

MIT License - see LICENSE file.

## Author

Sumit Raj
- M.Tech Applied AI & ML @ VNIT Nagpur
- Ex-Software Engineer Intern @ Salesforce
- GitHub: https://github.com/sumit966
- LinkedIn: https://www.linkedin.com/in/er-sumit-raj-/
- Portfolio: https://sumit966-github-io.vercel.app
- Email: info.sr0909@gmail.com

If you found this project useful, please consider giving it a star!
