from typing import List


"""
Unbounded Knapsack Problem
Time Complexity: O(N*M) where N=len(coins), M=amount
"""


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[amount] if dp[amount] != float("inf") else -1
