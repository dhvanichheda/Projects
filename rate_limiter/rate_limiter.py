#!/usr/bin/env python3 

import time 
from collections import defaultdict, deque
from queue import Queue
from typing import List

class RateLimiter:
    def __init__(self, limit: int, time_window: int):
        self.limit = limit
        self.time_window = time_window
        self.user_requests = Queue()

    def is_allowed(self, user_id: str, req_time: float) -> bool:
        current_time = time.time()

        while not self.user_requests.empty() and (current_time - self.user_requests.queue[0]) > self.time_window:
            self.user_requests.get()

        if self.user_requests.qsize() < self.limit:
            self.user_requests.put(req_time)
            return True
        else:
            return False


if __name__ == "__main__":
    rate_limiter = RateLimiter(5, 60)
    user_id = '1234'

    for i in range(7):
        now = time.time()
        allowed = rate_limiter.is_allowed(user_id, now)
        print(f'Request {i+1}: {'Allowed' if allowed else 'Denied'}')
        time.sleep(10)
