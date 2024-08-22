from typing import List

"""
number array (nums) allows duplicates
=> only by comparing nums[mid] and nums[l], it's hard to notify left or right sorted portion
=> we need to find the pivot index directly
"""


def search(self, nums: List[int], target: int) -> bool:
    def get_pivot():
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                # when nums[mid] == nums[r]
                # check if right is the pivot
                if r > 0 and nums[r - 1] > nums[r]:
                    return r
                # otherwise, move right pointer inward
                r -= 1
        return l

    def find_target(l, r):
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    pivot = get_pivot()
    # rotated array
    if pivot > 0:
        return find_target(0, pivot - 1) or find_target(pivot, len(nums) - 1)
    # not rotated array
    return find_target(0, len(nums) - 1)
