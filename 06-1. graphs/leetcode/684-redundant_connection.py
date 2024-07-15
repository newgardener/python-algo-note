from typing import List

# %%
"""
use DFS to find a cycle in undirected graph
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
