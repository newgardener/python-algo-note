# Definition for a binary tree node.
from typing import Optional

"""
N: # of node in BST

Time Complexity: O(N)
ㄴ process each node once in a constant time
Space Complexity: O(N) in the best case, O(logN) in the worst case
ㄴ height of BST due to call stack
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, sum_so_far):
            if not node:
                return sum_so_far
            sum_so_far = dfs(node.right, sum_so_far)
            sum_so_far += node.val
            node.val = sum_so_far
            sum_so_far = dfs(node.left, sum_so_far)
            return sum_so_far

        if not root:
            return root

        dfs(root, 0)
        return root
