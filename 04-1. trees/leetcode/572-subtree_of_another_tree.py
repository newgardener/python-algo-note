from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        # root and subRoot is the same tree
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and t2 and t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(
                t1.right, t2.right
            )
        return False
