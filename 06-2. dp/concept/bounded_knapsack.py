"""
W: max capacity of knapsack
weights: weight of each item
values: value of each item
"""


def boundedKnapsack(W, weights, values):
    n = len(weights)
    # initialize dp array from 0 to W
    dp = [0] * (W + 1)

    # consider each item one by one
    for i in range(n):
        # we need to go backwards to avoid using the same items multiple times
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]


def boundedKnapsack2D(W, weights, values):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if w >= weights[i - 1]:
                # not take it: dp[i-1][w]
                # take it: dp[i-1][w-weights[i-1]] + values[i-1]
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][2]
    return dp[n][W]
