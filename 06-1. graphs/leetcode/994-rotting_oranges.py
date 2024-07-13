import collections
from typing import List

"""
Take-Away:
problems involving simultaneous propagation or infection across a grid, "BFS" is usually more suitable than DFS
BFS = level-by-level traversal
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                # store rotten oranges
                if grid[i][j] == 2:
                    q.append((i, j))
                # count fresh oranges
                if grid[i][j] == 1:
                    fresh += 1

        while q and fresh >= 0:
            x, y, time = q.popleft()
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                # level-by-level propagation
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    # update status (grid state, fresh count)
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny))
        return time if fresh == 0 else -1
