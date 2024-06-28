from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def dfs(node):
            if not node:
                # height
                return 0

            lHeight = self.dfs(node.left)
            rHeight = self.dfs(node.right)
            self.maxDiameter = max(self.maxDiameter, lHeight + rHeight)
            return max(lHeight, rHeight) + 1

        dfs(root)
        return self.maxDiameter
