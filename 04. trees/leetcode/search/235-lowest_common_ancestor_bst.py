"""
Note: don't need to traverse the whole tree, split point is the LCA
Time Complexity: O(logN) height of the tree
Space Complexity: O(1)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# %%
class Solution:
    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # set p to be always smaller than q
        if p.val > q.val:
            p, q = q, p

        node = root
        while node:
            if q.val < node.val:
                node = node.left
            elif p.val > node.val:
                node = node.right
            else:
                return node


# %%

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        # base case
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # case 1 - p and q are in different subtrees
        if left and right:
            return root
        # case 2 - p and q are in the same subtree
        if left or right:
            return left if left else right
        # case 3 - p and q do not exist in this binary search tree
        return None
