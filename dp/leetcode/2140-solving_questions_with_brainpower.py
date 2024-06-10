from typing import List

"""
0-1 Knapsack Problem
Recursive Solution: Time Complexity O(2^N)
"""


def mostPointsRecursive(questions: List[List[int]]) -> int:
    dp = {}

    def dfs(i):
        if i >= len(questions):
            return 0

        if i in dp:
            return dp[i]

        dp[i] = max(dfs(i + 1), questions[i][0] + dfs(questions[i][1] + 1 + i))
        return dp[i]

    return dfs(0)


def mostPointsIterative(questions: List[List[int]]) -> int:
    # dict structure is useful - not getting out of range error
    dp = {}

    for i in range(len(questions) - 1, -1, -1):
        dp[i] = max(questions[i][0] + dp.get(questions[i][1] + 1 + i), dp.get(i + 1))

    return dp[0]
