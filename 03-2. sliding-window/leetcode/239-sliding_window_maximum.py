from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
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

        if r + 1 >= k:
            result.append(nums[q[0]])

    return result
