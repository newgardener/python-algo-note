from typing import List

"""
DP solution with postfix sum
"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # postfix_sum[i] meaning sum from index i to the end
        postfix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            postfix_sum[i] = postfix_sum[i + 1] + piles[i]

        memo = {}

        # choices: 1 <= X <= 2M, for each turn M=max(M,x)
        def dfs(i, m):
            if i >= n:
                return 0
            # caching
            if (i, m) in memo:
                return memo[(i, m)]
            # if possible, take it all
            if i + 2 * m >= n:
                return postfix_sum[i]

            # minimize opponent_sum
            opponent_sum = float('infinity')
            # possible range of choices [1, 2*m]
            for x in range(1, 2 * m + 1):
                opponent_sum = min(opponent_sum, dfs(i + x, max(m, x)))

            result = postfix_sum[i] - opponent_sum
            memo[(i, m)] = result
            return result

        # m starts with 1
        return dfs(0, 1)
