# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    numDict = {}
    for num in set(nums):
        if num not in numDict:
            if num - 1 in numDict:
                numDict[num] = numDict[num - 1] + 1
            else:
                numDict[num] = 1
            while num + 1 in numDict:
                numDict[num + 1] = numDict[num] + 1
                num += 1
    return max(list(numDict.values()))


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    numSet = set(nums)
    maxLength = 0

    for num in numSet:
        if num - 1 not in numSet:
            currNum = num
            currLength = 1

            while currNum + 1 in numSet:
                currNum += 1
                currLength += 1

            maxLength = max(maxLength, currLength)
    return maxLength
