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
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = (
                dp[i][j] + 1
                if text1[i] == text2[j]
                else max(dp[i - 1][j], dp[i][j - 1])
            )
    return dp[m][n]
