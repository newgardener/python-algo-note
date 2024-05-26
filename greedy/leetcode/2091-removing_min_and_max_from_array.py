from typing import List


def minimumDeletions(nums: List[int]) -> int:
    end = len(nums) - 1
    minVal, maxVal = min(nums), max(nums)
    minIndex, maxIndex = nums.index(minVal), nums.index(maxVal)
    mid = end // 2

    if minIndex <= mid and maxIndex <= mid:
        return max(minIndex + 1, maxIndex + 1)
    elif minIndex > mid and maxIndex > mid:
        return max(end - minIndex + 1, end - maxIndex + 1)

    leftSide = max(minIndex + 1, maxIndex + 1)
    rightSide = max(end - minIndex + 1, end - maxIndex + 1)
    combined = min(minIndex + 1, end - minIndex + 1) + min(
        maxIndex + 1, end - maxIndex + 1
    )
    return min(leftSide, rightSide, combined)
