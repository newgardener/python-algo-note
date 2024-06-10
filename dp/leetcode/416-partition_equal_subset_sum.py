from typing import List


def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    if target in nums:
        return True

    dp = set([0])

    for num in nums:
        newDp = set(dp)
        for t in dp:
            if t + num == target:
                return True
            newDp.add(t + num)
        dp = newDp
    return False
