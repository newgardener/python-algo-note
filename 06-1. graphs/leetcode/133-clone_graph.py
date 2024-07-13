from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional

# %%
"""
BFS approach:
- clonedNode hashmap keeps track of visited nodes and its clones
- iterate neighbors of each node and if not visited, create a clone and add to a queue
- this ensures we only go through each node once

Time Complexity:
N - number of nodes, E - number of edges
=> O(N+E)
"""


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        clonedNode = {node: Node(node.val)}
        q = deque([node])
        while q:
            current = q.popleft()
            for neighbor in current.neighbors:
                # neighbor not yet visited
                if neighbor not in clonedNode:
                    clonedNode[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clonedNode[current].neighbors.append(clonedNode[neighbor])
        return clonedNode[node]


# %%
# DFS approach
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
