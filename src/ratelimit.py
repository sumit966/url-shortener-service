"""Simple in-memory sliding-window rate limiter.

For single-instance deployments. For multi-instance, replace with Redis.
"""
import time
from collections import defaultdict, deque
from typing import Tuple


class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int = 60, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)

    def allow(self, key: str) -> Tuple[bool, int]:
        """Returns (allowed, remaining)."""
        now = time.time()
        cutoff = now - self.window_seconds
        q = self.requests[key]

        while q and q[0] < cutoff:
            q.popleft()

        if len(q) >= self.max_requests:
            return False, 0

        q.append(now)
        return True, self.max_requests - len(q)


limiter = SlidingWindowRateLimiter(max_requests=60, window_seconds=60)
