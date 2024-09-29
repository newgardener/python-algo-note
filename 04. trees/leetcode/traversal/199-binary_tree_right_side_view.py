import collections
from typing import Optional, List

"""
BFS == Level Order Traversal
Time Complexity: O(logN) - height of the tree
Key Point:
- add the right-most node of each level to the result 
- related to "Binary Tree Level Order Traversal" problem
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque([root])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if i == qLen - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
