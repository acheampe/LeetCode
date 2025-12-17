from collections import OrderedDict
import time


class TTLCacheLRU:
    def __init__(self, capacity=3):
        self.capacity = capacity
        # key -> (value, expires_at)
        self.store = OrderedDict()

    def set(self, key, value, ttl_seconds):
        #time uses wall clock which can be rolled back
        now = time.time() # should use perf_counter() to mitigate clock roll back error. 
        expires_at = now + ttl_seconds

        # Capacity checks should account for expired entries; otherwise valid data gets evicted unnecessarily.
        if len(self.store) >= self.capacity and key not in self.store:
            self.store.popitem(last=True) # last=True or even an empty arg will cause orderedDict to remove MRU instead of LRU (must take care to use 'last=False')

        if key in self.store:
            # two lines of code are not necessary since we want a complete refresh of val and expiration time
            old_value, old_expires_at = self.store[key]
            expires_at = old_expires_at # should not reuse old_expired
            
            # what is necessary here is moving the node to the tail of our LinkedList (move_to_end)
            # since updating values does not automatically reposition existing nodes

        self.store[key] = (value, expires_at)

    def get(self, key):
        if key not in self.store:
            return None # picky here but gracefully handling return so user can know what is happening (err msg) not req for MVP

        value, expires_at = self.store[key]
        now = time.perf_counter() # good use of perf_counter

        if now >= expires_at:
            # implement lazy removal of expired cache here, otherwise we will unintentially bloat up our hashmap with expired data
            return None

        # update MRU after get
        return value