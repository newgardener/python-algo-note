from typing import List


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
