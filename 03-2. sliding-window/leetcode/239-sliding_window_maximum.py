# %%
"""
MaxHeap
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""

import heapq


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    result = []
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        # shrink window size to k
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        if i >= k - 1:
            result.append(-heap[0][0])
    return result


# %%

"""
Monotonic Decreasing Queue
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    result = []
    q = deque()

    for r in range(len(nums)):
        # monotonic decreasing queue
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        # store the index of num
        q.append(r)

        # if number no longer inside the window
        if r - k == q[0]:
            q.popleft()

        # first element of the queue is the largest number within the window
        if r >= k - 1:
            result.append(nums[q[0]])

    return result
