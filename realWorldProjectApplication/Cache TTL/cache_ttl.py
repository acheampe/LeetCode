import time
from typing import Any


class TTLCache:
    def __init__(self):
        # key -> (value, expires_at)
        self._store: dict[Any, tuple[Any, float]] = {}

    def set(self, key: Any, value: Any, ttl_seconds: float) -> None:
        """
        Store a key with a value and a time-to-live (TTL).
        """
        expires_at = time.perf_counter() + ttl_seconds
        self._store[key] = (value, expires_at)

    def get(self, key: Any) -> Any:
        """
        Retrieve a value if it exists and has not expired.
        Returns None if the key is missing or expired.
        """
        if key not in self._store:
            return None

        value, expires_at = self._store[key]

        if time.perf_counter() >= expires_at:
            # Lazy expiration
            del self._store[key]
            return None

        return value