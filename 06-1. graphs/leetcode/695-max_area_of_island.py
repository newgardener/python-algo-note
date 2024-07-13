from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(i, j, area):
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            return (1 +
                    dfs(i - 1, j, area + 1) +
                    dfs(i + 1, j, area + 1) +
                    dfs(i, j - 1, area + 1) +
                    dfs(i, j + 1, area + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea = max(maxArea, dfs(i, j, 0))
        return maxArea
