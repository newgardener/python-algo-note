from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    numDict = {}
    for i, num in enumerate(numbers):
        if target - num in numDict:
            return [numDict[target - num], i + 1]
        numDict[num] = i + 1
