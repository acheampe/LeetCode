import time
from collections import deque
from typing import Any


class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int = 5, window_seconds: float = 10.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # key -> deque[timestamps]
        self._state: dict[Any, deque[float]] = {}

    def allow(self, key: Any) -> bool:
        now = time.time()

        if key not in self._state:
            self._state[key] = deque()
        
        window = self._state[key]
        cutoff = now - self.window_seconds

        while window and window[0] < cutoff:
            window.popleft()

        if len(window) <= self.max_requests:
            window.append(now)
            return True

        return False