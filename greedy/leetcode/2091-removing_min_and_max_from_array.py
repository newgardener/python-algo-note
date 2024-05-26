from typing import List


def minimumDeletions(nums: List[int]) -> int:
    end = len(nums)
    minIndex, maxIndex = nums.index(min(nums)), nums.index(max(nums))

    leftSide = max(minIndex + 1, maxIndex + 1)
    rightSide = max(end - minIndex, end - maxIndex)
    combined = min(minIndex + 1, end - minIndex) + min(maxIndex + 1, end - maxIndex)

    return min(leftSide, rightSide, combined)
