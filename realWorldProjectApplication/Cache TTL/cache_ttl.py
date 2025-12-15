from collections import OrderedDict
import time

class TTLCacheLRU:
    def __init__(self, capacity = 100):
        
        self.capacity = capacity
        self._storage = OrderedDict()
    
    def set(self, key, value, ttl):
        
        expires_at = time.perf_counter() + ttl
        
        if len(self._storage) >= self.capacity and key not in self._storage:
            # remove least recently used
            self._storage.popitem(last=False) 
        
        elif key in self._storage:
            self._storage.move_to_end(key) # makes existing key as MRU before update
        
        self._storage[key] = (value, expires_at) # automatically is marked as MRU if not in key
    
    def get(self, key):
        
        if key not in self._storage:
            return None
        
        val, expiration_time = self._storage[key]
        if time.perf_counter() >= expiration_time:
            del self._storage[key]
            return None

        self._storage.move_to_end(key) # MRU
        return val