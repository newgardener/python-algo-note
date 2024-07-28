from heapq import heappop, heappush
from typing import List

# %%
"""
Take-Away:
- think in backwards! trace back from the end goal to the start point
Time Complexity: O(N)
with no space complexity
"""


def canJump(self, nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        # move forward the end goal
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False


# %%
"""
It hits TLE why?
- it is considering all possible jumps at each index
  - which can lead to O(N^2) time complexity at worst
- how to iterate the array only once in order to make time complexity O(N)?
"""


def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    maxHeap = [(nums[0], 0)]  # (jump, index)
    while maxHeap:
        jump, index = heappop(maxHeap)
        if index == n - 1:
            return True
        if jump == 0:
            continue
        for i in range(index + 1, index + 1 + jump):
            heappush(maxHeap, (nums[i], i))
    return False
