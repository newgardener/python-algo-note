from collections import deque

"""
Both BFS, DFS approach ensures we go through each node once

Time Complexity:
N - number of nodes, E - number of edges
=> O(N+E)
"""


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
"""
DFS approach:
- clonedNode hashmap keeps track of visited nodes and its clones
- check if the node is cloned
- if not, recursively clones all neighbors of the node and returns the cloned node  
"""


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        clonedNode = {}

        def dfs(node):
            # base condition
            if node in clonedNode:
                return clonedNode[node]

            cloned = Node(node.val)
            clonedNode[node] = cloned
            for neighbor in node.neighbors:
                cloned.neighbors.append(dfs(neighbor))
            return cloned

        return dfs(node)
