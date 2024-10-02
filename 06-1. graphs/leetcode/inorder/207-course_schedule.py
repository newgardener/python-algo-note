from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inorder = [0] * numCourses

        for u, v in prerequisites:
            # v -> u
            graph[v].append(u)
            inorder[u] += 1

        # start with nodes that has no pre-req (inorder == 0)
        q = deque([i for i in range(numCourses) if inorder[i] == 0])
        cnt = 0
        while q:
            node = q.popleft()
            cnt += 1
            for neighbor in graph[node]:
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0:
                    q.append(neighbor)

        # whether we can finish courses or not
        return cnt == numCourses
