from typing import Optional

"""
Time Complexity: 
- while part: O(logN)
- depth of recursive function: O(logN)
=> O(logNlogN)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l, r = root, root
        lh, rh = 0, 0
        # calculate height of a left subtree
        while l:
            l = l.left
            lh += 1
        # calculate height of a right subtree
        while r:
            r = r.right
            rh += 1

        # perfect binary tree
        if lh == rh:
            return 2 ** lh - 1
        # complete binary tree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
