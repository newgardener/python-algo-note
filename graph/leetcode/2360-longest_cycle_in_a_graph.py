from collections import defaultdict, deque
from typing import List


class Solution:
    def buildGraph(self, edges):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for u, v in enumerate(edges):
            graph[u].append(v)
            in_degree[v] += 1
            if u not in in_degree:
                in_degree[u] = 0
        return graph, in_degree

    def topological_sort(self, n, graph, in_degree):
        topo_list = []
        visited = [False] * n
        queue = deque([node for node in in_degree if in_degree[node] == 0])

        while queue:
            node = queue.popleft()
            topo_list.append(node)
            visited[node] = True
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return topo_list, visited

    def calculateCycle(self, startNode, edges, visited):
        if visited[startNode]:
            return 0

        visited[startNode] = True
        cycle = 1
        nextNode = edges[startNode]
        while nextNode != startNode and not visited[nextNode]:
            visited[nextNode] = True
            cycle += 1
            nextNode = edges[nextNode]
        return cycle

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph, in_degree = self.buildGraph(edges)
        topo_list, visited = self.topological_sort(n, graph, in_degree)

        if all(visited):
            return -1

        nodeVisited = [False] * n
        longest_cycle = -1
        for i in range(n):
            if visited[i] == False:
                longest_cycle = max(
                    self.calculateCycle(i, edges, nodeVisited), longest_cycle
                )
        return longest_cycle
