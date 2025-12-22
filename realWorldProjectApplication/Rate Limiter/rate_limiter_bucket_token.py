import time
from typing import Any


class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        """
        capacity: max number of tokens in the bucket
        refill_rate: tokens added per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        # key -> (tokens, last_refill_time)
        self.buckets: dict[Any, tuple[float, float]] = {}

    def allow(self, key: Any) -> bool:
        now = time.perf_counter()

        if key not in self.buckets:
            # initialize bucket as full
            self.buckets[key] = (self.capacity - 1, now)
            return True

        tokens, last_refill = self.buckets[key]

        # refill tokens based on elapsed time
        elapsed = now - last_refill
        refill = elapsed * self.refill_rate
        tokens = min(self.capacity, tokens + refill)

        if tokens < 1:
            # no tokens available
            self.buckets[key] = (tokens, now)
            return False

        # consume one token
        tokens -= 1
        self.buckets[key] = (tokens, now)
        return True