# %%
# DFS + Memoization


def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
    size = len(strs)
    memo = {}

    def dfs(i, _m, _n):
        if i >= size:
            return 0

        skip = dfs(i + 1, _m, _n)
        zeroes = strs[i].count("0")
        ones = strs[i].count("1")
        if zeroes <= _m and ones <= _n:
            not_skip = dfs(i + 1, _m - zeroes, _n - ones)
            memo[(i, _m, _n)] = max(skip, not_skip)
        else:
            memo[(i, _m, _n)] = skip
        return memo[(i, _m, _n)]

    return dfs(0, m, n)


# %%
# 2D DP
"""
- a set of items are given
- find the max subset of items satisfying the constraints m and n 
ㄴ which is similar to knapsack 0-1 problem with constraint W
"""


def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
    n = len(strs)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for item in strs:
        zeroes = item.count("0")
        ones = item.count("1")
        for i in range(m, zeroes - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

    return dp[m][n]