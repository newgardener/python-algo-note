import collections
from collections import deque
from typing import List

"""
Take-Away:
problems involving simultaneous propagation or infection across a grid, "BFS" is usually more suitable than DFS
BFS = level-by-level traversal
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                # fresh
                if grid[i][j] == 1:
                    fresh += 1
                # rotten
                elif grid[i][j] == 2:
                    q.append((i, j))

        t = 0
        while q and fresh > 0:
            qLen = len(q)
            t += 1
            for _ in range(qLen):
                x, y = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2
                        q.append((nx, ny))

        return t if fresh == 0 else -1
