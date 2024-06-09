from typing import List


# solution using dict - Time Complexity: O(N)
def twoSum(numbers: List[int], target: int) -> List[int]:
    numDict = {}
    for i, num in enumerate(numbers):
        if target - num in numDict:
            return [numDict[target - num], i + 1]
        numDict[num] = i + 1


# solution using two pointers - Time Complexity: O(N)
def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        curSum = numbers[l] + numbers[r]
        mid = (l + r) // 2
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
