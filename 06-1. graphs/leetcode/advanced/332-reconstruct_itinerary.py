from collections import defaultdict
from typing import List

# %%
"""
DFS + Backtracking Solution => but hit TLE why?
N = # of tickets, K = max # of dst from src
Time Complexity: O(N^K) at worst it can explore all possible paths
Space Complexity: O(N)

"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        graph = defaultdict(list)
        ticketCnt = defaultdict(lambda: defaultdict(int))
        for frm, to in tickets:
            graph[frm].append(to)
            ticketCnt[frm][to] += 1

        for frm in graph:
            graph[frm].sort()  # sort in ascending order

        result = ["JFK"]

        def dfs(node):
            if len(result) == n + 1:
                return True

            if node not in graph:
                return False

            for nextNode in graph[node]:
                if ticketCnt[node][nextNode] > 0:
                    ticketCnt[node][nextNode] -= 1
                    result.append(nextNode)

                    if dfs(nextNode):
                        return True

                    # backtrack
                    ticketCnt[node][nextNode] += 1
                    result.pop()

            return False

        dfs("JFK")
        return result
