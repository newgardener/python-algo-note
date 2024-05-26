from typing import List


def minimumDeletions(nums: List[int]) -> int:
    n = len(nums)
    i, j = nums.index(min(nums)), nums.index(max(nums))
    return min(
        max(i, j) + 1,
        n - min(i, j),
        min(i, j) + 1 + (n - max(i, j)),
    )
