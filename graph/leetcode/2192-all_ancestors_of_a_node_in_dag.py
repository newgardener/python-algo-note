from collections import defaultdict
from typing import List


class Solution:
    def buildGraph(self, edges: List[List[int]]) -> defaultdict[int, list]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        return graph

    def findAncestors(
        self, node: int, graph: defaultdict[int, list], ancestors: List[set]
    ):
        if node not in graph:
            return
        for parent in graph[node]:
            ancestors[node].add(parent)
            self.findAncestors(parent, graph, ancestors)
            ancestors[node].update(ancestors[parent])

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        graph = self.buildGraph(edges)

        for node in range(n):
            self.findAncestors(node, graph, ancestors)

        return [sorted(list(ancestor)) for ancestor in ancestors]
