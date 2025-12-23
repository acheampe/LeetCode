
class RouteReq:
    def __init__(self):
        self._servers = { # server and load counter
            'A' : 0,
            'B' : 0,
            'C' : 0, 
        }
        self._key_to_server = {} # key -> server
        self._min_server_load = (float('inf'), '')
    
    def route_request(self, request_id: str) -> str:
        if request_id in self._key_to_server: 
            return self._key_to_server[request_id]
        
        self._min_server_load = (float('inf'), '')
        for server, load in self._servers.items():
            self._min_server_load = min(self._min_server_load, (load, server))
        
        _, min_server = self._min_server_load
        self._servers[min_server] += 1
        self._key_to_server[request_id] = min_server
        
        return min_server
            
            