from collections import deque
import heapq
import time
import asyncio

class TaskScheduler:
    def __init__(self):
        self.heap = []  # (execute_at, order, task)
        self.counter = 0

    def schedule(self, execute_at: float, task):
        heapq.heappush(self.heap, (execute_at, self.counter, task))
        self.counter += 1

    async def run(self):
        """Aysnc loop that executes scheduled tasks."""

        if not self.heap:
            return
        
        while self.heap:
            
            execute_time = self.heap[0][0]
            now = time.perf_counter()
            
            if now < execute_time:
                await asyncio.sleep(execute_time - now)
                continue
            
            _, _, execute_func = heapq.heappop(self.heap)

            asyncio.create_task(execute_func())
