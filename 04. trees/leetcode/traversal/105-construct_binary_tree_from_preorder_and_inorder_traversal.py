from typing import List, Optional

"""
Key Points:
- first element of preorder array is a root value
- if you find the root value in inorder array, left side would be a left subtree and vice versa
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        mid = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
ㅠ