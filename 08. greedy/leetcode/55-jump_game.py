from heapq import heappop, heappush
from typing import List

"""
It hits TLE why?
- it is considering all possible jumps at each index
  - which can lead to O(N^2) time complexity at worst
- how to iterate the array only once in order to make time complexity O(N)
"""


class Solution:
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
