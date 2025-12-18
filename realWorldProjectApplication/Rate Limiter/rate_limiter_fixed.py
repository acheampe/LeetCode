import time
from typing import Any


class FixedWindowRateLimiter:
    def __init__(self, max_requests: int = 5, window_seconds: float = 10.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # key -> (window_start, count)
        self._state: dict[Any, tuple[float, int]] = {}

    def allow(self, key: Any) -> bool:
        now = time.time()

        if key not in self._state:
            self._state[key] = (now, 1)
            return True

        window_start, count = self._state[key]

        # window reset logic
        if now - window_start > self.window_seconds:
            window_start = now
            count = 0

        # decision
        if count <= self.max_requests:
            count += 1
            self._state[key] = (window_start, count)
            return True

        self._state[key] = (window_start, count)
        return False