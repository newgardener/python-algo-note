from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = set()
        rotten = set()
        for i in range(m):
            for j in range(n):
                # fresh orange
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    rotten.add((i, j))

        def dfs(i, j, time):
            if (i, j) not in fresh:
                return time

            # make an orange rotten
            fresh.remove((i, j))
            return max(
                time,
                dfs(i - 1, j, time + 1),
                dfs(i + 1, j, time + 1),
                dfs(i, j - 1, time + 1),
                dfs(i, j + 1, time + 1)
            )

        maxMin = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i, j in rotten:
            for dx, dy in dirs:
                if (i + dx, j + dy) in fresh:
                    maxMin = max(maxMin, dfs(i + dx, j + dy, 1))
        return maxMin if not fresh else -1
