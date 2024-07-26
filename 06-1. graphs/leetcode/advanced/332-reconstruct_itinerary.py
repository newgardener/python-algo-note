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


# %%
"""
Hierholzer's Algorithm
Time Complexity:
- main algorithm part (while loop) is O(N) => each edge is processed only once
=> overall time complexity is O(NlogK) for sorting part
Space Complexity: O(N)

=> Hierholzer's Algorithm excels in time complexity compared to DFS + Backtracking Algorithm 
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        graph = defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)

        for frm in graph:
            graph[frm].sort(reverse=True)  # in order to get lexically smaller dst when popping

        stack = ["JFK"]
        res = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
