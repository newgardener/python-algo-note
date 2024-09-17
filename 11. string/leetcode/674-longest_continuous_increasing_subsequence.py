from typing import List

"""
Sliding Window
Time Complexity: O(N)
Space Complexity: O(1)
"""


def findLengthOfLCIS(nums: List[int]) -> int:
    res, left = 0, 0
    for i in range(len(nums)):
        if i and nums[i - 1] >= nums[i]:
            left = i
        res = max(res, i - left + 1)
    return res
