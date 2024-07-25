import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for frm, to, price in flights:
            graph[frm].append((to, price))

        # initialize distance of each node for (k+2) stops
        distances = [[float('infinity')] * (k + 1) for _ in range(n)]

        # (cost, city, stops)
        pq = [(0, src, 0)]
        while pq:
            cost, city, stops = heapq.heappop(pq)

            if city == dst:
                return cost
            # over k stops case
            if stops > k:
                continue
            # dijikstra's skip condition
            if cost < distances[city][stops]:
                continue

            # update distances
            distances[city][stops] = cost
            for neighbor, price in graph[city]:
                newCost = cost + price
                newStops = stops + 1
                if newCost < distances[neighbor][newStops]:
                    distances[neighbor][newStops] = newCost
                    heapq.heappush(pq, (newCost, neighbor, newStops))

        return -1
