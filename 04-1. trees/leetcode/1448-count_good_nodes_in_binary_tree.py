"""
Time Complexity: O(N)
where N is the number of nodes
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, pathMax):
            if not node:
                return 0
            cnt = 0
            if node.val >= pathMax:
                cnt += 1
            maxVal = max(pathMax, node.val)
            if node.left:
                cnt += dfs(node.left, maxVal)
            if node.right:
                cnt += dfs(node.right, maxVal)
            return cnt

        return dfs(root, float("-infinity"))
