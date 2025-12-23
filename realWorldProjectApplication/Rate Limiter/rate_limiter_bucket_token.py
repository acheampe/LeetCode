import time
import typing

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate: float):
        """
        capacity: max number of tokens in the bucket
        refill_rate: tokens added per second
        """
        
        self.capacity = capacity
        self.refill_rate: float = refill_rate
        self._track_rate: dict[typing.Any, tuple[float, int]]= {}
    
    def is_valid_request(self, user_id: typing.Any):
        
        if not user_id:
            return 'User_id not found'
        fill_time = time.perf_counter()

        if user_id not in self._track_rate:
            self._track_rate[user_id] = (fill_time, self.capacity)
            
        self.refill(user_id, fill_time)
        
        return self.is_allowed(user_id)
    
    def is_allowed(self, user_id: typing.Any) -> bool:
        
        last_filled, total_token = self._track_rate[user_id]
        
        if total_token > 0:
            self._track_rate[user_id] = (last_filled, total_token - 1)
            return True
        
        return False
    
    def refill(self, user_id, curr_fill_time):
        last_filled, total_token = self._track_rate[user_id]

        elapsed = curr_fill_time - last_filled
        to_add = int(elapsed * self.refill_rate)

        if to_add > 0:
            total_token = min(self.capacity, total_token + to_add)
            last_filled = last_filled + (to_add / self.refill_rate) # resets last_filled to now

        self._track_rate[user_id] = (last_filled, total_token)
        
            
        
