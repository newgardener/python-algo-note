from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_row1, prefix_row2 = grid[0].copy(), grid[1].copy()
        # prefix sum
        for i in range(1, n):
            prefix_row1[i] += prefix_row1[i - 1]
            prefix_row2[i] += prefix_row2[i - 1]

        res = 0
        for i in range(n):
            top = prefix_row1[-1] - prefix_row1[i]
            bottom = prefix_row2[i - 1]
            # robot2 will take the best among top and bottom
            secondRobot = max(top, bottom)
            # goal of robot1 is to minimize the points of robot2
            res = min(res, secondRobot)
        return res
