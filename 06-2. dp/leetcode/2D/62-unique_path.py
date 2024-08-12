"""
Time Complexity: O(m*n)
"""


# %%
# 2D DP
# Space Complexity: O(m*n)

def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0] * n for _ in range(m)]
    for i in range(n):
        dp[0][i] = 1
    for j in range(m):
        dp[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[m - 1][n - 1]


# %%
# 1D DP
# Space Complexity: O(n)

def uniquePaths(self, m: int, n: int) -> int:
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            # dp[j]: cell from a prev row (top)
            # dp[j-1]: cell from a current row (left)
            dp[j] += dp[j - 1]
    return dp[n - 1]
