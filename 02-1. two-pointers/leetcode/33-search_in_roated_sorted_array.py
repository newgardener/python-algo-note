from typing import List


# %%
"""
My Solution: do the binary search after finding pivot index
"""


def search(nums: List[int], target: int) -> int:
    last = len(nums) - 1
    pivot = last
    while nums[pivot - 1] < nums[pivot] and pivot >= 1:
        pivot -= 1

    l, r = 0, last
    if target <= nums[-1]:
        l, r = pivot, last
    else:
        l, r = 0, pivot - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


# %%
"""
Enhanced Solution: do the binary search w/o finding pivot index
"""


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1
