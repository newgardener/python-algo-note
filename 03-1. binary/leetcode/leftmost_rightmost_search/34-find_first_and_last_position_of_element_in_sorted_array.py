"""
Leftmost Search: O(logN)
Rightmost Search O(logN)
"""


def searchRange(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]

    # leftmost search
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    leftmost = l if l < len(nums) and nums[l] == target else -1

    # rightmost search
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    rightmost = l - 1 if l - 1 < len(nums) and nums[l - 1] == target else -1
    return [leftmost, rightmost]
