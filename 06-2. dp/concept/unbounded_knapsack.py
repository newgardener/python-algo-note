"""
W: max capacity of knapsack
weights: weight of each item
values: value of each item
"""


def unboundedKnapsack(W, weights, values):
    n = len(weights)
    dp = [0] * (W + 1)

    for w in range(1, W + 1):
        # we can use items unlimitedly
        for i in range(n):
            if w >= weights[i]:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]


def unboundedKnapsack2D(W, weights, values):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if w >= weights[i - 1]:
                # not take it: dp[i-1][w]
                # take it: dp[i][w-weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i - 1][w], dp[i][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]
