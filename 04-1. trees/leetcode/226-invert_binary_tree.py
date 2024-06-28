from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node):
            if not node:
                return None
            lnode = swap(node.left)
            rnode = swap(node.right)
            node.left, node.right = rnode, lnode
            return node

        return swap(root)
