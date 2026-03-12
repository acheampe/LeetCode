from collections import defaultdict
import heapq


class LogAggregation:
    def __init__(self):
        self.logged_data = defaultdict(lambda: defaultdict(int))

    def aggregate_logs(self, logs: list[str]):
        for log in logs:
            self.read_log(log)
        return self.logged_data

    def read_log(self, log: str):
        parts = log.split()
        service, log_level = parts[1], parts[2]
        self.logged_data[service][log_level] += 1

    def top_k_error(self, k: int, level: str = "ERROR") -> list[str]:
        min_heap = []

        for service, levels in self.logged_data.items():
            error_count = levels.get(level, 0)

            entry = (error_count, service)
            heapq.heappush(min_heap, entry)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))

        result.sort(key=lambda x: (-x[0], x[1]))
        return [service for _, service in result]
        
        
        
        
        
    # defaultdict(lambda:
    #     defaultdict(lambda:
    #         defaultdict(lambda:
    #             defaultdict(int)
    #         )))