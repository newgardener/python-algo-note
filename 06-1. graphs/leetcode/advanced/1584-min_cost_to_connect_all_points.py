import heapq
from typing import List

"""
create MST problem => apply Kruskal's algorithm
Time Complexity: 
- sort edges: O(ElogE) or at most O(ElogV)
Space Complexity: O(V)
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # create edges (pointX, pointY, manhattan distance)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, dist))

        parents = list(range(n))
        rank = [0] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            # already a union
            if px == py:
                return False
            # make them into a union
            if rank[px] > rank[py]:
                parents[py] = px
                rank[px] += rank[py]
            else:
                parents[px] = py
                rank[py] += rank[px]
            return True

        # sort edges in an ascending distance order
        edges.sort(key=lambda x: x[2])
        minCost = 0
        edgeCnt = 0
        for p1, p2, dist in edges:
            if union(p1, p2):
                minCost += dist
                edgeCnt += 1
                if edgeCnt == n - 1:
                    break

        return minCost
