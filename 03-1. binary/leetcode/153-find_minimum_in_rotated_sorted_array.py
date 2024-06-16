from typing import List

"""
Time Complexity: O(logN)
"""


def findMin(nums: List[int]) -> int:
    # edge case
    if nums[0] < nums[-1]:
        return nums[0]

    l, r = 0, len(nums) - 1
    # right-edged search
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= nums[0]:
            l = mid + 1
        else:
            r = mid - 1

    if l >= len(nums):
        return nums[-1]
    return nums[l]
