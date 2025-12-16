from collections import deque
from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class Job:
    job_id: str
    task: Callable[[], Any]
    retries: int = 0
    max_retries: int = 3


class JobQueue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, job: Job) -> None:
        self._queue.append(job)

    def dequeue(self) -> Job | None:
        if not self._queue:
            return None
        return self._queue.popleft()

    def is_empty(self) -> bool:
        return len(self._queue) == 0


class Worker:
    def __init__(self, queue: JobQueue):
        self.queue = queue

    def process_next(self) -> None:
        job = self.queue.dequeue()

        if not job:
            return

        try:
            print(f"Processing job {job.job_id}")
            job.task()
            print(f"Job {job.job_id} completed")

        except Exception as e:
            job.retries += 1
            print(f"Job {job.job_id} failed ({job.retries})")

            if job.retries <= job.max_retries:
                self.queue.enqueue(job)
            else:
                print(f"Job {job.job_id} permanently failed")