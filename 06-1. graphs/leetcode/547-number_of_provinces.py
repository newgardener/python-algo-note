from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = []
        for i in range(n):
            for j in range(n):
                if i != j and j > i and isConnected[i][j]:
                    edges.append((i, j))

        parents = list(range(n))
        rank = [0] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            # already union
            if px == py:
                return 0
            # make it a union
            if rank[px] > rank[py]:
                parents[py] = px
                rank[px] += rank[py]
            else:
                parents[px] = py
                rank[py] += rank[px]
            return 1

        res = n
        for u, v in edges:
            res -= union(u, v)
        return res
