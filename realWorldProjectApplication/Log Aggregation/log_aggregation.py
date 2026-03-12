from collections import defaultdict

class LogAggregation:
    def __init__(self):
        
        self.logged_data: defaultdict = defaultdict(lambda: defaultdict(int))
    
    def aggregate_logs(self, logs: list[str]):
        
        for log in logs:
            self.read_log(log)
        
        return self.logged_data
    
    def read_log(self, log: str):
        # 0: 2026-03-12T10:00:01 
        # 1: auth-service 
        # 2: ERROR 
        # 3: Failed 
        # 4: login 
        # 5: attempt
        parts = log.split(' ')
        
        self.logged_data[parts[1]][parts[2]] += 1
        
        
        
    
    