from typing import List

"""
Time Complexity: O(N * T) where N=len(nums) and T=sum(nums)
"""


# %%
# DFS + Memoization

def findTargetSumWays(nums: List[int], target: int) -> int:
    dp = {}

    def dfs(i, total):
        if i == len(nums):
            return 1 if total == target else 0

        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
        return dp[(i, total)]

    return dfs(0, 0)


# %%
# 2D DP

"""
sum(A): + set, sum(B): - set
sum(A) - sum(B) = target
sum(A) + sum(A) = target + sum(B) + sum(A)
sum(A) * 2 = target + sum(nums)
=> sum(A) = (target + sum(nums)) // 2

Define Problem with 0-1 knapsack template
dp[i][j] = 물건(=숫자) i개로 배낭 용량(=target) j를 채울 수 있는 방법 수 단, 각 물건은 한 번씩만 사용 가능 (=bounded knapsack)  
dp[n][numToReach]
"""


def findTargetSumWays(nums: List[int], target: int) -> int:
    total = sum(nums)
    n = len(nums)
    # edge case
    if total < abs(target) or (total + target) % 2 == 1:
        return 0
    numToReach = (total + target) // 2

    dp = [[0] * (numToReach + 1) for _ in range(n + 1)]
    # base case
    # 물건 i개로 용량 0을 채울 수 있는 방법은 1가지 => 배낭에 넣지 않기
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(numToReach + 1):
            # 용량이 충분할 때
            # dp[i-1][j]: 배낭에 넣지 않기
            # dp[i-1][j-nums[i-1]]: 배낭에 넣기
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
            # 용량이 부족할 때
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][numToReach]


# %%
# 1D DP

def findTargetSumWays(nums: List[int], target: int) -> int:
    total = sum(nums)
    n = len(nums)
    # edge case
    if total < abs(target) or (total + target) % 2 == 1:
        return 0
    numToReach = (total + target) // 2

    dp = [0] * (numToReach + 1)
    for i in range(n):
        # 이전 결과가 이후 결과에 영향을 미치면 안되기 때문에 역방향으로 순회 (각 숫자는 한 번씩만 사용 가능)
        for j in range(numToReach, -1, -1):
            if j >= nums[i]:
                # dp[j]: 배낭에 넣지 않기
                # dp[j-nums[i]]: 배낭에 넣기
                dp[j] = dp[j] + dp[j - nums[i]]
    return dp[numToReach]
