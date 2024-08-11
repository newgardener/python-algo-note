# %%
# 2D DP Solution

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case (from empty string to target character)
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        # dp (= bottom-up approach)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # matched
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # replace: dp[i-1][j-1]
                    # insert: dp[i][j-1]
                    # delete: dp[i-1][j]
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]


# %%

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            # caching
            if (i, j) in memo:
                return memo[(i, j)]

            # base case
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            # recursive (= top-down approach)
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(dp(i - 1, j - 1), dp(i - 1, j), dp(i, j - 1)) + 1
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)
