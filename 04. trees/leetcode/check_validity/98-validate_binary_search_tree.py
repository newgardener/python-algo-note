from typing import Optional

"""
Time Complexity: O(N)
Key Points:
- initial boundary should be -inf < x < inf
- left node boundary updated to left < x < node.val
- right node boundary updated to node.val < x < right
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return validate(node.left, left, node.val) and validate(node.right, node.val, right)

        return validate(root, float("-inf"), float("inf"))
