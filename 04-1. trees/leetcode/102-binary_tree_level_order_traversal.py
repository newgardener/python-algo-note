import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#%%
# dfs
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cache = collections.defaultdict(list)

        def dfs(node, level=0):
            if not node:
                return
            cache[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root)
        return [value for value in cache.values()]
