from collections import deque
from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class Job:
    job_id: str
    task: Callable[[], Any]
    retries: int = 0
    max_retries: int = 3
    # DESIGN GAP: No idempotency key or deduplication mechanism
    # Retried jobs may cause duplicate side effects if task is not idempotent


class JobQueue:
    def __init__(self):
        self._queue = deque()
        # BUG / DESIGN GAP: No thread-safety or concurrency control
        # Multiple workers accessing this queue could corrupt state

    def enqueue(self, job: Job) -> None:
        self._queue.append(job)
        # DESIGN GAP: No visibility timeout or in-flight tracking
        # If a worker crashes mid-job, the job is lost forever

    def dequeue(self) -> Job | None:
        if not self._queue:
            return None
        return self._queue.popleft()
        # DESIGN GAP: No acknowledgment mechanism
        # Once dequeued, the job is considered "gone" even if it fails catastrophically

    def is_empty(self) -> bool:
        return len(self._queue) == 0
        # MINOR: is_empty() is redundant — callers can directly check dequeue() result


class Worker:
    def __init__(self, queue: JobQueue):
        self.queue = queue
        # DESIGN GAP: No worker identity or concurrency limits
        # Hard to reason about parallel execution or load distribution

    def process_next(self) -> None:
        job = self.queue.dequeue()
        # BUG / DESIGN GAP: Job is removed from queue before processing
        # If process crashes here, job is permanently lost

        if not job:
            return

        try:
            print(f"Processing job {job.job_id}")
            job.task()
            # BUG: No timeout or cancellation handling
            # A long-running or hung task will block this worker indefinitely

            print(f"Job {job.job_id} completed")
            # DESIGN GAP: No acknowledgment or commit step
            # Success is implicit, which breaks at-least-once guarantees

        except Exception as e:
            job.retries += 1
            print(f"Job {job.job_id} failed ({job.retries})")
            # BUG: Retry count is incremented in memory only
            # If the process restarts, retry history is lost

            if job.retries <= job.max_retries:
                self.queue.enqueue(job)
                # BUG: Immediate retry causes hot-loop retries
                # No backoff, delay, or jitter implemented
            else:
                print(f"Job {job.job_id} permanently failed")
                # DESIGN GAP: Failed jobs are dropped silently
                # No dead-letter queue or observability hook