import time
from typing import Any

class RateLimiter:
    def __init__(self, max_request=5, window_seconds = 10):
        
        self.max_request = max_request
        self.window_seconds = window_seconds
        self._rate_tracker: dict[Any, tuple[float, int]] = {}
    
    def hit(self, key):
        """func to initiate new key and return True if not in rate_tracker
        else, is_hit func determines key hit viability
        """
        curr_time = time.perf_counter()
        
        if key not in self._rate_tracker:
            self._rate_tracker[key] = (curr_time, 1)
            return True

        return self.is_hit(key, curr_time)
    
    def is_hit(self, key, curr_time_stamp):
        """func to determine if key hit is True or False given time window and max request limit"""
        
        start_time, total_request = self._rate_tracker[key]
        expired_window = curr_time_stamp - start_time 
        
        if expired_window < self.window_seconds and total_request < self.max_request:
            self._rate_tracker[key] = (start_time, total_request + 1) # update counter 
            return True
        
        elif expired_window >= self.window_seconds: # reset counter condition and timer
            self._rate_tracker[key] = (curr_time_stamp, 1)
            return True
        
        return False