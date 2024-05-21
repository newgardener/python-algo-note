from typing import List


def binarySearch(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target[mid] == target:
            return mid
        elif target[mid] > target:
            right = mid - 1
        elif target[mid] < target:
            left = mid + 1
    return -1


def leftBoundedBinarySearch(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target[mid] == target or target[mid] > target:
            right = mid - 1
        elif target[mid] < target:
            left = mid + 1

    if left >= len(nums) or nums[left] != target:
        return -1
    return left


def rightBoundedBinarySearch(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target[mid] == target or target[mid] < target:
            left = mid + 1
        elif target[mid] > target:
            right = mid - 1

    if right < 0 or nums[right] != target:
        return -1
    return right
