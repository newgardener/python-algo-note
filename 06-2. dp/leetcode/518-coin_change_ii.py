from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # base case
        # i개의 동전을 이용해 금액 0을 만드는 방법 => 동전 안쓰기
        for i in range(n + 1):
            dp[i][0] = 1
        # i개의 동전을 이용해 금액 0을 만드는 방법 => 없음
        for j in range(amount + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for w in range(1, amount + 1):
                if w >= coins[i - 1]:
                    dp[i][w] = dp[i - 1][w] + dp[i][w - coins[i - 1]]
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][amount]
