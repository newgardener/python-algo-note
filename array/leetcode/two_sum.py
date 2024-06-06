from typing import List


def twoSumInSortedArray(nums: List[int], target: int) -> List[int]:
    i, j = 0, len(nums) - 1

    while not i == j:
        numSum = nums[i] + nums[j]
        if numSum == target:
            return [i, j]
        elif numSum > target:
            j -= 1
        else:
            i += 1


def twoSumInUnSortedArray(nums: List[int], target: int) -> List[int]:
    numMap = {}
    for i, num in enumerate(nums):
        if target - num in numMap:
            return [numMap[target - num], i]
        numMap[num] = i
