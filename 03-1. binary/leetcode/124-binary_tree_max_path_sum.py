from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def isLeafNode(node):
            return node and not node.left and not node.right

        maxSum = float("-inf")

        def dfs(node):
            nonlocal maxSum

            if isLeafNode(node):
                return node.val

            lSum = dfs(node.left) if node.left else float("-inf")
            rSum = dfs(node.right) if node.right else float("-inf")
            maxSum = max(maxSum, lSum + rSum + node.val, lSum, rSum)
            return max(max(lSum, rSum) + node.val, node.val)

        result = dfs(root)
        return max(result, maxSum)
