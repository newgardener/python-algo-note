from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)

        def binarySearch(left, right, target=0):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right < 0 or nums[right] > target:
                return -1
            return right

        left, right = 0, len(nums) - 1
        rightmost = binarySearch(left, right)
        neg, pos = nums[: rightmost + 1], nums[rightmost + 1 :]

        if neg[-1] < 0:
            return max(len(neg), len(pos))
        else:
            if nums[0] == 0:
                return len(pos)
            idx = len(neg) - 1
            while neg[idx] == 0 and idx > 0:
                idx -= 1

            return max(len(nums[: idx + 1]), len(pos))
