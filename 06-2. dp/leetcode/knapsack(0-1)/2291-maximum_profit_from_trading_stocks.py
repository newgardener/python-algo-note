def maximumProfit(present: list[int], future: list[int], budget: int) -> int:
    n = len(present)
    W = budget
    dp = [0] * (W + 1)
    values = [f - p for p, f in zip(present, future)]

    for i in range(n):
        # we can decide within the range of current stock price (present)
        for w in range(W, present[i]-1, -1):
            if w >= present[i]:
                dp[w] = max(dp[w], dp[w - present[i]] + values[i])
