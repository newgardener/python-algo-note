from typing import List

"""
Unbounded Knapsack Problem
Time Complexity: O(N*M) where N=len(coins), M=amount
"""


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    # i개의 coin 중 가장 적은 수의 coin을 사용해서 금액 w를 만들 수 있는 방법
    for i in range(len(coins)):
        for w in range(1, amount + 1):
            if w >= i:
                dp[w] = min(dp[w], 1 + dp[w - coins[i]])

    return dp[amount] if dp[amount] != float("inf") else -1
