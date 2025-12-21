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
        # BUG / RISK: time.time() uses wall-clock time and can move backward or forward
        # A monotonic clock (e.g., time.perf_counter()) is safer for rate limiting logic

        if key not in self._state:
            self._state[key] = deque()
            # DESIGN GAP: No TTL or cleanup strategy for inactive keys
            # Keys with no future requests will remain in memory indefinitely

        window = self._state[key]
        cutoff = now - self.window_seconds

        while window and window[0] < cutoff:
            window.popleft()
            # DESIGN CHOICE: This is lazy cleanup (only happens on access)
            # Acceptable for MVP, but memory can grow at scale

        if len(window) <= self.max_requests:
            # BUG: Off-by-one error
            # When len(window) == max_requests, this still allows one more request
            # Correct condition should be len(window) < max_requests
            window.append(now)
            return True

        # DESIGN GAP: When window becomes empty after cleanup,
        # the key remains in self._state instead of being removed
        # This can cause unbounded key growth (memory leak)

        return False