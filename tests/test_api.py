"""Tests for URL Shortener API."""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200


def test_health():
    r = client.get("/health")
    assert r.status_code == 200


def test_shorten_valid():
    r = client.post("/shorten", json={"url": "https://example.com/some/long/path"})
    assert r.status_code == 200
    body = r.json()
    assert "code" in body
    assert body["short_url"].endswith(body["code"])


def test_shorten_invalid_url():
    r = client.post("/shorten", json={"url": "not-a-url"})
    assert r.status_code == 400


def test_shorten_idempotent():
    url = "https://example.com/idempotent-test"
    r1 = client.post("/shorten", json={"url": url})
    r2 = client.post("/shorten", json={"url": url})
    assert r1.status_code == 200
    assert r2.status_code == 200
    assert r1.json()["code"] == r2.json()["code"]


def test_custom_code():
    r = client.post("/shorten", json={"url": "https://example.com/custom", "custom_code": "mytest01"})
    assert r.status_code == 200
    assert r.json()["code"] == "mytest01"


def test_redirect():
    r = client.post("/shorten", json={"url": "https://example.com/redirect-test"})
    code = r.json()["code"]
    r2 = client.get(f"/{code}", follow_redirects=False)
    assert r2.status_code == 307


def test_analytics():
    r = client.post("/shorten", json={"url": "https://example.com/analytics-test"})
    code = r.json()["code"]
    client.get(f"/{code}", follow_redirects=False)
    client.get(f"/{code}", follow_redirects=False)
    r2 = client.get(f"/analytics/{code}")
    assert r2.status_code == 200
    assert r2.json()["total_clicks"] >= 2
