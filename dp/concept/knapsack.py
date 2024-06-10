"""
W: max capacity of knapsack
weights: weight of each item
values: value of each item
"""


def unboundedKnapSack(W, weights, values):
    # initialize dp array from 0 to W
    dp = [0] * (W + 1)

    for i in range(W + 1):
        for j in range(len(weights)):
            if weights[j] <= i:
                # take it or not take it
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
    return dp[W]
