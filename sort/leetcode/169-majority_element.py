"""
Time Complexity: 
    - O(n) for counting for each subArray
    - O(logn) for dividing arrays into subArrays
Space Complexity: O(1)
"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    def findMajority(start, end):
        # base condition for only one element
        if start == end:
            return nums[start]

        mid = (start + end) // 2

        leftMajority = findMajority(start, mid)
        rightMajority = findMajority(mid + 1, end)

        # if both halves have the same majority element
        if leftMajority == rightMajority:
            return leftMajority

        leftCount = nums[start : end + 1].count(leftMajority)
        rightCont = nums[start : end + 1].count(rightMajority)

        return leftMajority if leftCount > rightCont else rightMajority

    return findMajority(0, len(nums) - 1)
