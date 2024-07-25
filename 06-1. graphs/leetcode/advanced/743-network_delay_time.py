import heapq
from collections import defaultdict
from typing import List

"""
shortest path from source to target node -> Dijikstra's algorithm
Time Complexity: O((V+E)logV)
Space Complexity: O(V)
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        distances = {node: float('infinity') for node in range(1, n + 1)}
        while pq:
            dist, node = heapq.heappop(pq)
            # skip if distances[node] is smaller
            if dist > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                distance = dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(pq, (distance, neighbor))

            res = max(list(distances.values()))
            return res if res != float('infinity') else -1
