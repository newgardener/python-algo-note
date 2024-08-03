import heapq
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        pq = []
        m, n = len(grid), len(grid[0])
        # add starting points from grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    pq.append((0, i, j))

        while pq:
            dist, x, y = heapq.heappop(pq)

            # skip condition for dijikstra's
            if dist > grid[x][y]:
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                newDist = dist + 1
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1:
                    if dist + 1 < grid[nx][ny]:
                        grid[nx][ny] = newDist
                        heapq.heappush(pq, (newDist, nx, ny))
