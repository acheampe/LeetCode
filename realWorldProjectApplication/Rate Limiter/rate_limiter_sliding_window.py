import time
from typing import Any
from collections import deque

# Sliding window to eliminate burst calls at edges 
class RateLimiter:
    def __init__(self, max_request: int = 5, window_seconds: float = 10):
        self.max_request = max_request
        self.window_seconds = window_seconds
        self._rate_tracker: dict[Any, deque[float]] = {}

    def hit(self, key: Any) -> bool:
        now = time.perf_counter()

        if key not in self._rate_tracker:
            self._rate_tracker[key] = deque()
            self._rate_tracker[key].append(now)
            return True

        return self._is_hit(key, now)

    def _is_hit(self, key: Any, now: float) -> bool:
        window = self._rate_tracker[key]
        cutoff = now - self.window_seconds

        # Remove stale timestamps
        while window and window[0] < cutoff:
            window.popleft()

        if len(window) < self.max_request:
            window.append(now)
            return True

        return False
