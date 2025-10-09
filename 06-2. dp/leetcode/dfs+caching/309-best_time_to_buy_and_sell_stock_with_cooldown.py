"""
Time Complexity: O(N)
ㄴ without memoization, it would be O(2^N)
Space Complexity: O(N)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = {}

        def dfs(i, buying):
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            # option1 - buy or cooldown
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            # option2 - sell or cooldown
            else:
                # should have one cooldown session after selling the stock (i -> i + 2)
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
