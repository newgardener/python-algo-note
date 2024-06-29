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
