from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return abs(left - right) <= 1

    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left) + 1
        right = self.getHeight(node.right) + 1
        return max(left, right)
