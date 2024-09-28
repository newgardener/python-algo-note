from typing import List

"""
Sliding Window
Time Complexity: O(N)
Space Complexity: O(1)
"""


def findLengthOfLCIS(nums: List[int]) -> int:
    l = 0
    res = 0
    for r in range(len(nums)):
        if r > 0 and nums[r - 1] >= nums[r]:
            l = r
        res = max(res, r - l + 1)
    return res
