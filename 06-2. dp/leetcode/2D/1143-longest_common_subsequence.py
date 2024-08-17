# %%
# 2D

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    n, m = len(text1), len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text2[i - 1] == text1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# %%
# 1D

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    n, m = len(text1), len(text2)

    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if text2[i - 1] == text1[j - 1]:
                dp[j] = prev + 1
            else:
                # dp[j]: cell from prev row
                # dp[j-1]: prev cell in the same row
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp
    return dp[n]
