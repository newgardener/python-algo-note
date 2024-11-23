from typing import Optional

"""
# of root nodes: N, # of subRoot nodes: M
Time Complexity: O(N*M)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# separation of concerns: subtree matching, tree traversal
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. subtree matching
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            # check only relevant subtrees starting from the potential matches in the root tree
            # avoid unnecessary search
            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False

        # 2. tree traversal
        if not root:
            return False
        # check if root node's subtree matches with subRoot
        if dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
