from collections import defaultdict
from typing import List

# %%
"""
Union-Find Solution
"""


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


# %%
"""
DFS Solution
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        visited = set()

        # undirected graph
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)

        def dfs(node):
            for cnode in graph[node]:
                if cnode not in visited:
                    visited.add(cnode)
                    dfs(cnode)

        cnt = 0
        for node in graph:
            if node not in visited:
                cnt += 1
                visited.add(node)
                dfs(node)
        return cnt
