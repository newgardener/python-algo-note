# %%


# Recursion
# Time complexity: O(2^n)
def lengthOfLISRecursive(nums: list[int]) -> int:
    def dfs(i, j):
        if i == len(nums):
            return 0

        LIS = dfs(i + 1, j)  # not include
        if j == -1 or nums[j] < nums[i]:
            LIS = max(LIS, 1 + dfs(i + 1, i))
        return LIS

    return dfs(0, -1)


# %%


# DP (Top-Down Approach)
# Time Complexity: O(n^2)
def lengthOfLISTopDown(nums: list[int]) -> int:
    n = len(nums)
    memo = [[-1] * (n + 1) for _ in range(n)]

    def dfs(i, j):
        if i == n:
            return 0
        if memo[i][j + 1] != -1:
            return memo[i][j + 1]

        LIS = dfs(i + 1, j)  # not include
        if j == -1 or nums[j] < nums[i]:
            LIS = max(LIS, 1 + dfs(i + 1, j))
        memo[i][j + 1] = LIS
        return LIS

    return dfs(0, -1)


# %%


# DP (Bottom-Up Approach)
# Time Complexity: O(n^2)
def lengthOfLISBottomUp(nums: list[int]) -> int:
    n = len(nums)
    LIS = [1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)
