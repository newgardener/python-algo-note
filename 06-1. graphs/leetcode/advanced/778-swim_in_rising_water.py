import heapq
from typing import List

"""
target: find the path with minimum maximum height => Dijikstra's algorithm with a PQ
Time Complexity: O(logN) where N is the grid dimension
Space Complexity: O(N^2)
"""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        minTime = 0

        while pq:
            # use priority queue to pop the smallest grid at a time
            t, x, y = heapq.heappop(pq)
            minTime = max(minTime, t)
            # reach the bottom right square
            if x == n - 1 and y == n - 1:
                break
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))

        return minTime
