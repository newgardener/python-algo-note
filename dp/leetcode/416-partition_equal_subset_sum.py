from typing import List


def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    if target in nums:
        return True

    def dfs(i, target):
        # base condition
        if target == 0:
            return True
        if i == len(nums) or target < 0:
            return False

        notTake = dfs(i + 1, target)
        take = dfs(i + 1, target - nums[i])
        res = notTake or take

        return res

    return dfs(0, target)
