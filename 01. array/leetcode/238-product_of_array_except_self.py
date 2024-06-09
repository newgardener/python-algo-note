from typing import List

"""
Requirement: O(N) Time Complexity, O(1) Space Complexity
"""


def productExceptSelf(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]
    post = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] = post
        post *= nums[j]
    return res
