from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inorder = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            inorder[u] += 1

        q = deque([i for i in range(numCourses) if inorder[i] == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in graph[node]:
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []
