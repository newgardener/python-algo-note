from collections import Counter, deque
import heapq
from typing import List


# each task 1 unit time
# purpose is to minimize idle time
def leastInterval(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()  # pairs of [-cnt, idleTime]

    while maxHeap or q:
        time += 1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])

        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time
