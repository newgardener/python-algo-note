from typing import List


# %%
def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    target = sum(nums) // 2
    if target in nums:
        return True

    dp = {0}

    for num in nums:
        newDp = set(dp)
        for t in dp:
            if t + num == target:
                return True
            newDp.add(t + num)
        dp = newDp
    return False


# %%
# 2D DP

def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    if sum(nums) % 2:
        return False
    target = sum(nums) // 2

    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # base case
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]


# %%
# 1D DP

def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    if sum(nums) % 2:
        return False
    target = sum(nums) // 2

    dp = [False] * (target + 1)
    dp[0] = True
    for i in range(n):
        for j in range(target, -1, -1):
            if j >= nums[i]:
                dp[j] = dp[j] or dp[j - nums[i]]
    return dp[target]
