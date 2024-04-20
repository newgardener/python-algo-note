# %%
n = 5
# 역방향 순회
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        print(i, j)

# %%

# 대각선 순회
for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = l + i - 1
        print(i, j)


# %%
def longestCommonSequence(text1: str, text2: str) -> int:
    n, m = len(text1) + 1, len(text2) + 1
    dp = [[0] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n - 1][m - 1]
