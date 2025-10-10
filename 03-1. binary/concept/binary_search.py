from typing import List


# %%
def binarySearch(nums: List[int], target: int):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # while loop ends when left == right
    return left if nums[left] == target else -1


def _binarySearch(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1


# %%
def leftmostBinarySearch(nums: List[int], target: int):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        # split into [left, mid), [mid+1, right)
        if nums[mid] == target or nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    # while loop ends when left == right
    # case 1 - out of bound case
    if left == len(nums):
        return -1
    # case 2 - check whether target matches
    return left if nums[left] == target else -1


# %%
def rightmostBinarySearch(nums: List[int], target: int):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        # split into [left, mid), [mid+1, right)
        if nums[mid] == target or nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    # while loop ends when left == right
    # case 1 - no target case
    if left == 0:
        return -1
    # case 2 - check whether target matches
    return left if nums[left - 1] == target else -1
