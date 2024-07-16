from typing import List

"""
Time Complexity:
- find(x): recursively finds the root of x with path compression with O(a(n))
- union(x, y): unites the sets containing x and y using union by rank with O(a(n))
=> O(m * a(n)) where m is the number of edges and a is the inverse Ackermann function 
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            # already in the same union
            if px == py:
                return 0

            # union process
            if rank[px] > rank[py]:
                parent[py] = px
            elif rank[py] > rank[px]:
                parent[px] = py
            else:
                parent[py] = px
                rank[px] += 1
            return 1

        # if edges do not share the same parent,
        # # of connected components == # of edges
        res = n
        for u, v in edges:
            res -= union(u, v)
        return res
