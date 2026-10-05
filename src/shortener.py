"""Short code generation + validation."""
import string
import secrets
import hashlib
from typing import Optional


ALPHABET = string.ascii_letters + string.digits  # 62 chars


def generate_short_code(length: int = 7) -> str:
    """Generate a random short code."""
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def generate_deterministic_code(url: str, length: int = 7) -> str:
    """Deterministic short code from URL hash (for idempotent shorten)."""
    h = hashlib.sha256(url.encode()).hexdigest()
    # Convert hex to base62-ish
    n = int(h, 16)
    chars = []
    for _ in range(length):
        n, rem = divmod(n, 62)
        chars.append(ALPHABET[rem])
    return "".join(chars)


def is_valid_url(url: str) -> bool:
    """Basic URL validation."""
    if not url or len(url) > 2048:
        return False
    return url.startswith(("http://", "https://"))


def is_valid_code(code: str) -> bool:
    """Validate short code format."""
    if not code or len(code) > 12:
        return False
    return all(c in ALPHABET for c in code)
