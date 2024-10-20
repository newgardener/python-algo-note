from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countUnivalSubtrees(root: Optional[TreeNode]) -> int:
    counts = 0

    def dfs(node):
        nonlocal counts
        if not node:
            return True

        left = True
        right = True
        if node.left:
            left = dfs(node.left) and node.val == node.left.val
        if node.right:
            right = dfs(node.right) and node.val == node.right.val

        if left and right:
            counts += 1
            return True
        return False

    dfs(root)
    return counts
