import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        pq = [(0, points[0])]
        distances = [float('infinity')] * n
        distances[0] = 0

        while pq:
            index, pos = heapq.heappop(pq)
            x1, y1 = pos
            for i in range(index + 1, n):
                x2, y2 = points[i]
                md = abs(x1 - x2) + abs(y1 - y2)
                if md < distances[i]:
                    distances[i] = md
                    heapq.heappush(pq, (i, points[i]))

        return sum(distances)
