from typing import Optional

"""
Key Points:
- should check every node that it is balanced
- should record 1) whether it is balanced so far, 2) maxHeight so far
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # (isBalanced, maxHeight)
        def dfs(node):
            if not node:
                return (True, 0)
            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)
            return (
                leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1,
                max(leftHeight, rightHeight) + 1,
            )

        return dfs(root)[0]
