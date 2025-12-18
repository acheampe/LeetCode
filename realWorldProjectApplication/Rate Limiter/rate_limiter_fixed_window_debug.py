import time
from typing import Any


class FixedWindowRateLimiter:
    def __init__(self, max_requests: int = 5, window_seconds: float = 10.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # key -> (window_start, count)
        self._state: dict[Any, tuple[float, int]] = {}

    def allow(self, key: Any) -> bool:
        now = time.time() # I would utilize perf_counter to avoid roll back errors here
        

        if key not in self._state:
            # expires_at = now + window_seconds
            self._state[key] = (now, 1) # though 'now' is ok, I would calc expires_at to simplify calc logic later and reduce 'now' ambuigiuity
            return True

        window_start, count = self._state[key]

        # window reset logic
        if now - window_start > self.window_seconds: # we want >= window_seconds, that way expiration happens at window_seconds
            # personal preference for readability: time.perf_counter() >= expires_at:
            window_start = now
            count = 0

        # decision
        if count <= self.max_requests: # no need for =, otherwise it will permit an additional count
            count += 1
            self._state[key] = (window_start, count)
            return True

        self._state[key] = (window_start, count) # I do not find this line to be necessary for application to work, 
        # given that false hits will not need to be updated and True hits will update key values before return
        return False