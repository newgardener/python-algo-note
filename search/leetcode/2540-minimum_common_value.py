from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def binarySearch(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums1[mid] == target:
                    return target
                elif nums1[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        left, right = 0, len(nums1) - 1
        for target in nums2:
            result = binarySearch(left, right, target)
            if result != -1:
                return result
        return -1
