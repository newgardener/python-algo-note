from typing import Optional

"""
Key Points:
- maxDiameter could be either a path including the node or not
- should pass the height of a subtree upwards
    - height of a subtree = max(leftHeight, rightHeight) + 1
"""


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

            lHeight = dfs(node.left)
            rHeight = dfs(node.right)
            self.maxDiameter = max(self.maxDiameter, lHeight + rHeight)
            return max(lHeight, rHeight) + 1

        dfs(root)
        return self.maxDiameter
