from typing import List


# %%
# 2D DP Solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # base case
        # i개의 동전을 이용해 금액 0을 만드는 방법 => 동전 안쓰기
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for w in range(amount + 1):
                if w >= coins[i - 1]:
                    dp[i][w] = dp[i - 1][w] + dp[i][w - coins[i - 1]]
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][amount]


# %%
# 1D DP Solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        # base case: 금액 0을 만드는 방법 => 동전 안쓰기
        dp[0] = 1
        for i in range(len(coins)):
            for w in range(1, amount + 1):
                if w >= coins[i]:
                    dp[w] += dp[w - coins[i]]
        return dp[amount]
