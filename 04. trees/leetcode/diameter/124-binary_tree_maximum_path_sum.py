from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:
    path_sum = float("-infinity")

    def dfs(node):
        nonlocal path_sum

        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        path_sum = max(
            path_sum, left + right + node.val, node.val, node.val + max(left, right)
        )
        return max(node.val, node.val + max(left, right))

    dfs(root)
    return path_sum
