# Scalable URL Shortener Service

Production-style URL shortener with rate limiting, click analytics, custom short codes, and idempotent shortening. Built with FastAPI and SQLite, designed for easy upgrade to Redis + PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Redis](https://img.shields.io/badge/Redis_(optional)-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## Overview

A URL shortener that goes beyond the naive "hash and store" approach:

1. **Idempotent shortening** - same URL returns same short code (no duplicates)
2. **Custom short codes** - users can pick their own alias
3. **Collision-safe random codes** - retries on collision, 62^7 keyspace
4. **Rate limiting** - sliding window, 60 requests per minute per IP
5. **Click tracking** - user agent, referrer, and timestamp per redirect
6. **Analytics** - total clicks, last 7 days, daily breakdown, top referrers
7. **Admin delete** - protected by a header token

Every redirect records a click so you can see how links perform over time.

## Problem Statement

A URL shortener looks trivial but has real engineering challenges:

- **Duplicate storage** - shortening the same URL twice should not create two codes
- **Collisions** - random codes can collide; must retry safely
- **Abuse** - without rate limiting, bots can flood the service
- **Analytics** - knowing click counts is not enough; you need time series and referrers
- **Custom codes** - must validate and check uniqueness

This project addresses each.

## Solution

A FastAPI service with:

- POST /shorten: idempotent shortening with optional custom code
- GET /{code}: 307 redirect + click recording
- GET /analytics/{code}: full analytics response
- Sliding-window rate limiter per client IP
- Admin delete with header-based token
- SQLite schema with indexed clicks table for fast analytics queries

## Architecture

Client
  |
  |-- POST /shorten --> Rate Limiter --> Idempotency Check
  |                                          |
  |                                          v
  |                                     Generate Code
  |                                     (or custom)
  |                                          |
  |                                          v
  |                                     SQLite (urls)
  |                                          |
  |                                          v
  |                                     Return short_url
  |
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

custom_code is optional. Omit it for a random 7-char code.

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

curl -I http://localhost:8000/myalias

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

curl -X DELETE http://localhost:8000/urls/myalias \
  -H "X-Admin: admin-secret"

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

For multi-instance deployments, swap the in-memory limiter for Redis (see optional deps).

## Analytics Details

Every redirect records:

- Timestamp (UTC)
- User-Agent header
- Referer header

Aggregated queries return:

- Total click count
- Clicks in the last 7 days
- Day-by-day breakdown for the last 7 days
- Top 5 referrers

The clicks table is indexed on code and clicked_at for fast aggregation.

## Testing

pytest tests/ -v

Tests cover:
- Root and health endpoints
- Shorten with valid URL
- Shorten with invalid URL returns 400
- Idempotent shorten returns same code
- Custom code path
- Redirect returns 307
- Analytics records clicks correctly

## Docker

Build:
docker build -t url-shortener .

Run:
docker run -p 8000:8000 url-shortener

## Production Upgrade Path

The project is structured to swap components without rewriting endpoints:

| Component | Dev | Production |
|-----------|-----|------------|
| Storage | SQLite | PostgreSQL |
| Rate limit | In-memory | Redis |
| Cache | None | Redis (redirect cache) |
| Analytics | SQL aggregate | Pre-aggregated tables |

Install requirements-optional.txt for the production stack.

## CI/CD

Every push to main triggers GitHub Actions:

1. Install Python 3.11 + dependencies
2. Run pytest test suite

See .github/workflows/ci.yml.

## Key Learnings

- Idempotent shortening requires a reverse lookup on original_url
- Random code collisions need a bounded retry loop, not infinite retries
- Sliding window beats fixed window for rate limiting accuracy
- Indexed clicks table keeps analytics queries fast even at millions of rows
- 307 preserves the HTTP method; 301 is cached by browsers and hides analytics
- Custom codes need format + uniqueness validation before storage
- Admin actions should be gated by header or token, not query params

## Future Improvements

- Redis-backed rate limiter for multi-instance scaling
- QR code generation for each short URL
- Expiring links (TTL field)
- User accounts with API keys
- Custom domains per user
- Bulk shorten (JSON array of URLs)
- Prometheus metrics + Grafana dashboard
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
