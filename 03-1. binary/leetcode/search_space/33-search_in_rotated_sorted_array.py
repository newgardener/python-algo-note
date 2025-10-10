from typing import List

"""
given N is len(nums),
Time complexity: O(logN)
Space complexity: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the leftmost rotation index
        def leftmost():
            l, r = 0, len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] <= nums[-1]:
                    r = mid
                else:
                    l = mid + 1
            return l

        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        rotate = leftmost()
        if nums[rotate] == target:
            return rotate
        if rotate == 0:
            return binary_search(0, len(nums) - 1)
        if nums[0] <= target <= nums[rotate - 1]:
            return binary_search(0, rotate - 1)
        return binary_search(rotate, len(nums) - 1)


