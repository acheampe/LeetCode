from collections import OrderedDict
import time


class TTLCacheLRU:
    def __init__(self, capacity=3):
        self.capacity = capacity
        # key -> (value, expires_at)
        self.store = OrderedDict()

    def set(self, key, value, ttl_seconds):
        now = time.time()
        expires_at = now + ttl_seconds

        if len(self.store) >= self.capacity and key not in self.store:
            self.store.popitem(last=True)

        if key in self.store:
            old_value, old_expires_at = self.store[key]
            expires_at = old_expires_at

        self.store[key] = (value, expires_at)

    def get(self, key):
        if key not in self.store:
            return None

        value, expires_at = self.store[key]
        now = time.perf_counter()

        if now >= expires_at:
            return None

        return value