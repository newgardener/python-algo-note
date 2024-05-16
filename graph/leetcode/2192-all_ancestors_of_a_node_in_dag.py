from collections import defaultdict, deque
from typing import List


class Solution:
    def buildGraph(self, n: int, edges: List[List[int]]) -> defaultdict[int, list]:
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        return graph, in_degree

    def topologicalSort(self, n: int, graph: dict[int, list], in_degree: List[int]):
        ordered_list = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            ordered_list.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return ordered_list

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph, in_degree = self.buildGraph(n, edges)
        ordered_list = self.topologicalSort(n, graph, in_degree)
        ancestors = [set() for _ in range(n)]

        for node in ordered_list:
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])

        return [sorted(list(ancestor)) for ancestor in ancestors]
