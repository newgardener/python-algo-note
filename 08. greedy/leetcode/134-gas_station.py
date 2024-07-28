from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return - 1

        startIndices = [index for index, value in enumerate(cost) if cost[index] <= gas[index]]
        for idx in startIndices:
            start = idx
            fuel = gas[idx]
            result = True
            for i in range(start, start + n):
                i = i % n
                if fuel < cost[i]:
                    result = False
                    break
                fuel = fuel + gas[(i + 1) % n] - cost[i]

            if result == True:
                return start if fuel >= cost[start] else -1

        return - 1
