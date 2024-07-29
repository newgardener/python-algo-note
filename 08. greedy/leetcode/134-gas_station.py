from typing import List

"""
Take-Away:
- early return an impossible case
- for each step, record a surplus and if we cannot make it at point i, move onto i+1 

greedy approach can make a big time complexity enhancement O(N^2) -> O(N)
Time Complexity: O(N)
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # cannot complete case
        if sum(gas) < sum(cost):
            return - 1

        # can complete case
        start = 0  # starting point
        total = 0  # record surplus
        for i in range(n):
            total += gas[i] - cost[i]

            # reset
            if total < 0:
                total = 0
                start = i + 1

        return start
