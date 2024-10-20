from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def equalToDescendants(root: Optional[TreeNode]) -> int:
    counts = 0

    def dfs(node):
        nonlocal counts
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        # count nodes equal to the sum of its descendants
        if node.val == left + right:
            counts += 1
        return node.val + left + right

    dfs(root)
    return counts
