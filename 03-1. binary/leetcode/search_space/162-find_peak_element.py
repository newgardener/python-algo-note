from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # we are checking a pair of element (mid, mid+1), so set our search space bounded
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
