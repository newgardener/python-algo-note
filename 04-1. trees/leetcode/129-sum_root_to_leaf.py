# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# %%
"""
solve using bfs
"""


def sumNumbers(root: Optional[TreeNode]) -> int:
    def isLeafNode(node):
        return node and not node.left and not node.right

    # (node, path)
    q = deque([(root, str(root.val))])
    result = []
    while q:
        node, path = q.popleft()
        if isLeafNode(node):
            result.append(int(path))
            continue
        if node.left:
            q.append((node.left, path + str(node.left.val)))
        if node.right:
            q.append((node.right, path + str(node.right.val)))
    return sum(result)


# %%
"""
solve using dfs
"""


def sumNumbers(root: Optional[TreeNode]) -> int:
    def dfs(node, pathSum):
        if not node:
            return 0

        pathSum = pathSum * 10 + node.val
        if not node.left and not node.right:
            return pathSum

        return dfs(node.left, pathSum) + dfs(node.right, pathSum)

    return dfs(root, 0)
