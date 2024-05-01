from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def addOneRow(
    self, root: Optional[TreeNode], val: int, depth: int
) -> Optional[TreeNode]:
    def bfs(node, level=1):
        if not node:
            return
        if level == depth - 1:
            # add new node no matter what current node has child or not
            oldLeft, oldRight = node.left, node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = oldLeft
            node.right.right = oldRight
            return
        bfs(node.left, level + 1)
        bfs(node.right, level + 1)

    if not root:
        return root

    if depth == 1:
        newRoot = TreeNode(val)
        newRoot.left = root
        return newRoot

    bfs(root)
    return root
