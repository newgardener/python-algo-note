from collections import Counter, deque
import heapq
from typing import List

"""
Time Complexity:
K = # of unique tasks, N = # of tasks
- initial heap creation: O(K)
- while loop: O(NlogK), but in worst case O(NlogN)

=> best/average case: O(N) when K is small and constant
=> worst case: O(NlogN)
"""


# each task 1 unit time
# purpose is to minimize idle time
def leastInterval(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque([])  # pairs of [-cnt, idleTime]

    while maxHeap or q:
        time += 1
        if maxHeap:
            # execute task
            cnt = 1 + heapq.heappop(maxHeap)
            # schedule next task
            if cnt:
                q.append([cnt, time + n])

        # if cooling time is met, push to maxHeap
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time
