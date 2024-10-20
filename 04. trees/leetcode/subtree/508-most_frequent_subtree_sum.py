from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findFrequentTreeSum(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    freq = defaultdict(int)
    def dfs(node):
        if not node:
            return 0

        treeSum = node.val + dfs(node.left) + dfs(node.right)
        freq[treeSum] += 1
        return treeSum

    dfs(root)
    maxVal = max(freq.values())
    return [k for k, v in freq.items() if v == maxVal]