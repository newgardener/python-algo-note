from typing import List


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
