from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # we move mid + 2 when a pair matched, so we set our search space bounded
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # in order to check pairs of element
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        # while loop exits when l == r
        return nums[l]
