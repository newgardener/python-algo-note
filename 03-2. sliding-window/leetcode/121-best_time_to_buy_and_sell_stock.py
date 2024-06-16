from typing import List

"""
Time Complexity: O(N)
"""


def maxProfit(prices: List[int]) -> int:
    buy = prices[0]
    profit = 0
    for i, price in enumerate(prices[1:]):
        if price < buy:
            buy = price
        else:
            profit = max(profit, price - buy)
    return profit
