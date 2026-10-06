<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- 🔗 Scalable URL Shortener — Full Animated README -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24,30&height=220&section=header&text=🔗%20URL%20Shortener%20Service&fontSize=46&fontColor=ffffff&animation=scaleIn&fontAlignY=40&desc=FastAPI%20·%20Rate%20Limiting%20·%20Analytics%20·%20Idempotent&descAlignY=60&descSize=17" />

</div>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=800&color=3B82F6&center=true&vCenter=true&multiline=true&width=800&height=100&lines=🔗+Scalable+URL+Shortener;⚡+Idempotent+%2B+Custom+Codes;📊+Click+Analytics+%2B+Rate+Limiting;🚀+FastAPI+%2B+SQLite+(Redis-ready)" alt="Typing SVG" />
</div>

<br/>

<div align="center">
  <a href="https://github.com/sumit966/url-shortener-service/stargazers">
    <img src="https://img.shields.io/github/stars/sumit966/url-shortener-service?style=for-the-badge&color=8b5cf6&labelColor=0d1117&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/url-shortener-service/network/members">
    <img src="https://img.shields.io/github/forks/sumit966/url-shortener-service?style=for-the-badge&color=3b82f6&labelColor=0d1117&logo=git&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/url-shortener-service/issues">
    <img src="https://img.shields.io/github/issues/sumit966/url-shortener-service?style=for-the-badge&color=ec4899&labelColor=0d1117&logo=github&logoColor=white" />
  </a>
  <a href="https://github.com/sumit966/url-shortener-service/commits/main">
    <img src="https://img.shields.io/github/last-commit/sumit966/url-shortener-service?style=for-the-badge&color=10b981&labelColor=0d1117&logo=git&logoColor=white" />
  </a>
</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge&logo=opensourceinitiative&logoColor=white" />
</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Rate_Limit-60_req%2Fmin-10b981?style=for-the-badge&logo=speedtest&logoColor=white" />
  <img src="https://img.shields.io/badge/Keyspace-62^7-8b5cf6?style=for-the-badge&logo=key&logoColor=white" />
  <img src="https://img.shields.io/badge/Redirect-307_Temporary-3b82f6?style=for-the-badge&logo=redirect&logoColor=white" />
  <img src="https://img.shields.io/badge/Analytics-Daily+Ref-ec4899?style=for-the-badge&logo=googleanalytics&logoColor=white" />
</div>

<br/>

<div align="center">
  <i>⚙️ Backend Engineering Project · Author: <b>Sumit Raj</b> · M.Tech VNIT Nagpur</i>
</div>

<br/>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />

---

## 📑 Table of Contents

<div align="center">

| 🔗 | 🎯 | 🏗️ |
|:---:|:---:|:---:|
| [Overview](#-overview) | [Problem](#-problem-statement) | [Solution](#-solution) |
| [Architecture](#-architecture) | [Tech Stack](#-tech-stack) | [Structure](#-project-structure) |
| [Quick Start](#-quick-start) | [API Usage](#-api-usage) | [Rate Limiting](#-rate-limiting) |
| [Analytics](#-analytics-details) | [Testing](#-testing) | [Docker](#-docker) |
| [Production Path](#-production-upgrade-path) | [Learnings](#-key-learnings) | [Future](#-future-improvements) |

</div>

---

## 🎯 Overview

<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="400" alt="Coding animation"/>
</div>

<br/>

A URL shortener that goes beyond naive **"hash and store"**:

<table align="center">
<tr>
<td width="33%" valign="top" align="center">

### 🔄 Idempotent

<img src="https://img.shields.io/badge/♻️-Same_URL_Same_Code-8b5cf6?style=for-the-badge" />

Same URL returns the same short code

</td>
<td width="33%" valign="top" align="center">

### 🎨 Custom Codes

<img src="https://img.shields.io/badge/✏️-User_Alias-10b981?style=for-the-badge" />

Users can pick their own alias

</td>
<td width="33%" valign="top" align="center">

### 🛡️ Collision-Safe

<img src="https://img.shields.io/badge/🔐-62^7_Keyspace-ef4444?style=for-the-badge" />

Retries on collision, huge keyspace

</td>
</tr>
<tr>
<td width="33%" valign="top" align="center">

### ⚡ Rate Limiting

<img src="https://img.shields.io/badge/🚦-60_req%2Fmin-3b82f6?style=for-the-badge" />

Sliding window per IP

</td>
<td width="33%" valign="top" align="center">

### 📊 Click Tracking

<img src="https://img.shields.io/badge/👆-UA_+_Ref-f59e0b?style=for-the-badge" />

User agent, referrer, timestamp

</td>
<td width="33%" valign="top" align="center">

### 📈 Analytics

<img src="https://img.shields.io/badge/📊-Daily_Breakdown-ec4899?style=for-the-badge" />

Total clicks, 7-day, top referrers

</td>
</tr>
</table>

<br/>

<div align="center">

### 🔐 Admin Delete

<img src="https://img.shields.io/badge/🛡️-Header_Token_Protected-8b5cf6?style=for-the-badge" />

</div>

---

## 🎯 Problem Statement

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=500&size=18&duration=3000&pause=1000&color=EF4444&center=true&vCenter=true&width=700&height=60&lines=⚠️+A+URL+shortener+looks+trivial...;⚠️+But+has+real+engineering+challenges!" alt="Problem intro" />
</div>

<br/>

<table align="center">
<tr>
<td width="50%" valign="top">

### ⚠️ Real Challenges

- 📦 **Duplicate storage** — same URL twice → two codes
- 💥 **Collisions** — random codes can collide
- 🚨 **Abuse** — bots can flood without rate limits
- 📊 **Analytics** — clicks alone aren't enough
- ✏️ **Custom codes** — must validate & check uniqueness

</td>
<td width="50%" valign="top">

### ✅ Our Approach

- ♻️ **Idempotency** via reverse lookup on URL
- 🔐 **Bounded retry loop** on collisions
- ⚡ **Sliding-window rate limiter** per IP
- 📈 **Time-series + referrer** analytics
- 🎨 **Custom code validation** with uniqueness check

</td>
</tr>
</table>

---

## ✨ Solution

A FastAPI service with:

```mermaid
flowchart LR
    A[👤 Client] --> B[🌐 FastAPI]
    B --> C[⚡ Rate Limiter]
    B --> D[🔗 Shortener]
    B --> E[💾 Storage]
    B --> F[📊 Analytics]
    C --> G{🚦 Allowed?}
    G -->|No| H[❌ 429]
    G -->|Yes| D
    D --> E
    E --> I[🗄️ SQLite urls]
    E --> J[📈 SQLite clicks]
    F --> J
    
    style A fill:#8b5cf6,stroke:#fff,color:#fff
    style H fill:#ef4444,stroke:#fff,color:#fff
    style I fill:#3b82f6,stroke:#fff,color:#fff
    style J fill:#10b981,stroke:#fff,color:#fff
```

<br/>

<table align="center">
<tr>
<td width="50%" valign="top">

### 🔗 Endpoints

- 🔵 `POST /shorten` — idempotent, custom code
- 🟢 `GET /{code}` — 307 redirect + click record
- 🟠 `GET /analytics/{code}` — full analytics
- 🟣 `GET /urls?limit=100` — list recent URLs
- 🔴 `DELETE /urls/{code}` — admin (header token)

</td>
<td width="50%" valign="top">

### 🛠️ Features

- ⚡ **Sliding-window rate limiter** per IP
- 🔐 **Admin delete** with header token
- 🗄️ **SQLite schema** with indexed clicks
- 🔄 **Collision-safe** retry loop
- ♻️ **Idempotent** on duplicate URLs

</td>
</tr>
</table>

---

## 🏗️ Architecture

### 🌐 Request Flow

```mermaid
sequenceDiagram
    participant C as 👤 Client
    participant R as ⚡ Rate Limiter
    participant S as 🔗 Shortener
    participant DB as 🗄️ SQLite
    
    C->>R: POST /shorten
    R->>R: Check sliding window
    alt Rate limit exceeded
        R-->>C: ❌ 429 Too Many Requests
    else Allowed
        R->>S: Forward request
        S->>DB: Lookup original_url
        alt URL exists
            DB-->>S: Return existing code
        else New URL
            S->>S: Generate unique code
            S->>DB: INSERT into urls
        end
        S-->>C: ✅ Return short_url
    end
```

### 📊 Redirect + Analytics Flow

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant API as 🌐 FastAPI
    participant DB as 🗄️ SQLite
    
    U->>API: GET /{code}
    API->>DB: Lookup code
    DB-->>API: Original URL
    API->>DB: INSERT click (UA + referrer + time)
    API-->>U: 🔄 307 Redirect
    
    Note over U,DB: Analytics Query
    U->>API: GET /analytics/{code}
    API->>DB: Aggregate clicks by day
    DB-->>API: Total, 7-day, daily, top refs
    API-->>U: 📊 JSON analytics
```

### 📐 ASCII Fallback

```
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
```

---

## 🛠️ Tech Stack

<table align="center">
<tr>
<td><b>Category</b></td>
<td><b>Technologies</b></td>
</tr>
<tr>
<td>🌐 API</td>
<td>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Uvicorn-2C2C2C?style=flat-square" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" />
</td>
</tr>
<tr>
<td>💾 Storage</td>
<td><img src="https://img.shields.io/badge/SQLite_(indexed)-003B57?style=flat-square&logo=sqlite&logoColor=white" /></td>
</tr>
<tr>
<td>⚡ Rate Limiting</td>
<td><img src="https://img.shields.io/badge/In--memory_sliding_window-3b82f6?style=flat-square" /></td>
</tr>
<tr>
<td>🧪 Testing</td>
<td>
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/httpx-3b82f6?style=flat-square" />
</td>
</tr>
<tr>
<td>🚀 Optional Upgrade</td>
<td>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" />
</td>
</tr>
<tr>
<td>🐳 Containerization</td>
<td><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /></td>
</tr>
<tr>
<td>⚙️ CI/CD</td>
<td><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" /></td>
</tr>
<tr>
<td>🐍 Language</td>
<td><img src="https://img.shields.io/badge/Python_3.11+-3776AB?style=flat-square&logo=python&logoColor=white" /></td>
</tr>
</table>

---

## 📁 Project Structure

```
url-shortener-service/
├── 🐍 src/
│   ├── __init__.py
│   ├── 🔗 shortener.py        # Code generation + validation
│   ├── 💾 storage.py          # SQLite schema + CRUD + analytics
│   └── ⚡ ratelimit.py        # Sliding-window limiter
├── 🌐 api/
│   ├── __init__.py
│   └── main.py                # FastAPI endpoints
├── 🧪 tests/
│   ├── __init__.py
│   └── test_api.py            # pytest tests
├── 📊 data/                   # SQLite db (git-ignored)
├── ⚙️ .github/workflows/ci.yml
├── 🐳 Dockerfile
├── 📋 requirements.txt
├── 📋 requirements-optional.txt
├── 🔐 .env.example
├── 🚫 .gitignore
├── 📜 LICENSE
└── 📖 README.md
```

---

## 🚀 Quick Start

<div align="center">
  <img src="https://img.shields.io/badge/⏱️_2_min_setup-3776AB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🐍_Python_3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</div>

<br/>

### 1️⃣ Clone

```bash
git clone https://github.com/sumit966/url-shortener-service.git
cd url-shortener-service
```

### 2️⃣ Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the API

```bash
uvicorn api.main:app --reload
```

**Runs at:** http://localhost:8000

### 5️⃣ Open Swagger

```bash
http://localhost:8000/docs
```

---

## 🎮 API Usage

### 🔵 POST `/shorten`

**Request:**

```json
{
  "url": "https://example.com/some/long/path",
  "custom_code": "myalias"
}
```

**Response:**

```json
{
  "code": "myalias",
  "short_url": "http://localhost:8000/myalias",
  "original_url": "https://example.com/some/long/path",
  "created_at": "2025-01-15T10:30:00"
}
```

> 💡 **Idempotent:** sending the same URL again returns the same code.

### 🟢 GET `/{code}`

Redirects **(307)** to the original URL and records a click with **user agent + referrer**.

### 🟠 GET `/analytics/{code}`

**Response:**

```json
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
```

### 🟣 GET `/urls?limit=100`

List the most recent URLs with click counts.

### 🔴 DELETE `/urls/{code}`

Delete a URL and its click history. Requires admin header.

```bash
curl -X DELETE http://localhost:8000/urls/myalias -H "X-Admin: admin-secret"
```

### 📋 Other Endpoints

| Endpoint | Method | Purpose |
|----------|:------:|---------|
| 🔵 `/` | 🟢 GET | API info |
| 💚 `/health` | 🟢 GET | Health check |
| 📘 `/docs` | 🟢 GET | Swagger UI |
| 📗 `/redoc` | 🟢 GET | Alternative docs |

---

## ⚡ Rate Limiting

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=18&duration=2500&pause=600&color=10B981&center=true&vCenter=true&width=600&height=50&lines=🚦+Sliding+Window+Rate+Limiter;🚦+60+requests+%2F+60+seconds+%2F+IP" alt="Rate Limit" />
</div>

<br/>

<table align="center">
<tr>
<td width="50%" valign="top">

### 🛡️ Rules

- ⏱️ **Sliding window:** 60 requests / 60 seconds
- 🌐 **Per client IP**
- 🎯 **Applied to:** `POST /shorten`
- ❌ **Returns 429** when exceeded

</td>
<td width="50%" valign="top">

### 💡 Why Sliding Window?

- ✅ **More accurate** than fixed window
- ✅ **No burst** at window boundaries
- ✅ **Fair** distribution over time
- ✅ **Simple** to implement in-memory

</td>
</tr>
</table>

---

## 📊 Analytics Details

<div align="center">
  <img src="https://img.shields.io/badge/📈_Every_Click_Recorded-8b5cf6?style=for-the-badge" />
</div>

<br/>

```mermaid
flowchart TD
    A[👆 Click] --> B[📝 Record]
    B --> C[⏰ Timestamp]
    B --> D[🌐 User Agent]
    B --> E[🔗 Referrer]
    C --> F[(🗄️ clicks table)]
    D --> F
    E --> F
    F --> G[📊 Aggregate]
    G --> H[📈 Total Clicks]
    G --> I[📅 Last 7 Days]
    G --> J[📉 Daily Breakdown]
    G --> K[🏆 Top 5 Referrers]
    
    style A fill:#8b5cf6,stroke:#fff,color:#fff
    style F fill:#3b82f6,stroke:#fff,color:#fff
    style H fill:#10b981,stroke:#fff,color:#fff
    style K fill:#f59e0b,stroke:#fff,color:#fff
```

<br/>

Every redirect records **timestamp, user-agent, and referer**. Aggregated queries return:

- 📈 **Total clicks**
- 📅 **Clicks in the last 7 days**
- 📉 **Day-by-day breakdown**
- 🏆 **Top 5 referrers**

> 💡 The `clicks` table is **indexed on `code` and `clicked_at`** for fast aggregation.

---

## 🧪 Testing

```bash
pytest tests/ -v
```

**Tests cover:**

- ✅ Root
- 💚 Health
- 🔵 Shorten valid
- ❌ Invalid URL returns 400
- ♻️ Idempotent shorten
- 🎨 Custom code
- 🔄 Redirect 307
- 📊 Analytics

---

## 🐳 Docker

### 🔨 Build

```bash
docker build -t url-shortener .
```

### ▶️ Run

```bash
docker run -p 8000:8000 url-shortener
```

---

## 📈 Production Upgrade Path

```mermaid
flowchart LR
    A[🛠️ Dev] --> B[🚀 Production]
    A1[💾 SQLite] --> B1[🐘 PostgreSQL]
    A2[⚡ In-memory limit] --> B2[🔴 Redis limiter]
    A3[🚫 No cache] --> B3[🔴 Redis cache]
    A4[📊 SQL aggregate] --> B4[📈 Pre-agg tables]
    
    style A fill:#3b82f6,stroke:#fff,color:#fff
    style B fill:#10b981,stroke:#fff,color:#fff
```

| Component | Dev | Production |
|-----------|-----|------------|
| 💾 Storage | SQLite | **PostgreSQL** |
| ⚡ Rate limit | In-memory | **Redis** |
| 🚀 Cache | None | **Redis (redirect cache)** |
| 📊 Analytics | SQL aggregate | **Pre-aggregated tables** |

---

## ⚙️ CI/CD

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=18&duration=2500&pause=600&color=2088FF&center=true&vCenter=true&width=700&height=50&lines=🚀+Every+push+to+main;🚀+GitHub+Actions+installs+deps+%26+runs+pytest" alt="CI" />
</div>

---

## 💡 Key Learnings

<table align="center">
<tr>
<td width="50%" valign="top">

### 🎓 Engineering Insights

- ♻️ **Idempotent shortening** requires reverse lookup on `original_url`
- 💥 **Random code collisions** need a bounded retry loop
- ⚡ **Sliding window** beats fixed window for accuracy
- 🗄️ **Indexed clicks table** keeps analytics fast at millions of rows
- 🔄 **307 preserves HTTP method**; 301 is cached and hides analytics
- 🔐 **Admin actions** should be gated by header, not query params

</td>
<td width="50%" valign="top">

### 🎯 Why These Matter

- 📊 **Scale:** Everything optimized for millions of rows
- 🛡️ **Security:** Header-based admin gating prevents CSRF
- 📈 **Accuracy:** Sliding window > fixed window
- 🔄 **Correctness:** 307 > 301 for analytics visibility
- ♻️ **Idempotency:** Same input → same output always
- 🎯 **Bounded retry:** Prevents infinite loops

</td>
</tr>
</table>

---

## 🚀 Future Improvements

<div align="center">

| 🌟 | Feature |
|:--:|---------|
| 🔴 | **Redis-backed rate limiter** for multi-instance scaling |
| 📱 | **QR code generation** for each short URL |
| ⏰ | **Expiring links** (TTL) |
| 👤 | **User accounts** with API keys |
| 📦 | **Bulk shorten** (JSON array) |
| 📊 | **Prometheus metrics** + Grafana |
| ☁️ | **Deploy to GCP Cloud Run** with Cloud SQL + Memorystore |

</div>

---

## 👤 Author

<div align="center">

<img src="https://img.shields.io/badge/Sumit_Raj-Backend_Engineer-3b82f6?style=for-the-badge&labelColor=0d1117" />

<br/><br/>

<b>M.Tech Applied AI & ML @ VNIT Nagpur</b><br/>
<i>Ex-Software Engineer Intern @ Salesforce</i>

<br/><br/>

<a href="https://sumit966.github.io">
  <img src="https://img.shields.io/badge/Portfolio-Visit-3b82f6?style=for-the-badge&logo=googlechrome&logoColor=white" />
</a>
<a href="https://www.linkedin.com/in/er-sumit-raj-/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="https://github.com/sumit966">
  <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>
<a href="mailto:info.sr0909@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<br/><br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=500&size=16&duration=3000&pause=1000&color=F59E0B&center=true&vCenter=true&width=600&height=50&lines=⭐+If+you+found+this+project+useful;⭐+Please+consider+giving+it+a+star!" alt="Star CTA" />

</div>

---

## 📄 License

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24,30&height=2&width=60%" />

<br/>

<img src="https://img.shields.io/badge/⚖️_LICENSE-MIT-f59e0b?style=for-the-badge&labelColor=0d1117&logo=opensourceinitiative&logoColor=white" />

<br/><br/>

<samp>
Released under the <b>MIT License</b> — see <a href="LICENSE">LICENSE</a> file.
</samp>

<br/><br/>

<sub><samp>© 2025 &nbsp;·&nbsp; SUMIT RAJ &nbsp;·&nbsp; ALL RIGHTS RESERVED</samp></sub>

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24,30&height=2&width=60%" />

</div>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24,30&height=120&section=footer&text=🔗%20Short%20URLs%20·%20Big%20Impact&fontSize=20&fontColor=ffffff&animation=scaleIn" width="100%" />
