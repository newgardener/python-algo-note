from typing import List

# %%
"""
use DFS to find a cycle in undirected graph
Time Complexity: O(n^2)
- dfs runs on n number of edges and each dfs takes O(n) of time 
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]

        def dfs(source, target):
            # base condition: found a cycle
            if source == target:
                return True
            seen.add(source)
            for neighbor in graph[source]:
                if neighbor not in seen and dfs(neighbor, target):
                    return True
            return False

        for u, v in edges:
            seen = set()
            if dfs(u, v):
                return [u, v]
            # undirected graph
            graph[u].append(v)
            graph[v].append(u)


# %%
"""
Time Complexity: O(n * a(n)) 
- union-find handles find operation with a(n) time complexity where a is the inverse Ackermann function, 
which grows very slowly and is effectively constant for all practical values in n
"""


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        # if we add this edge, we make a cycle
        if px == py:
            return False
        # union edges
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]

        return []
