import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# minDepth -> bfs
def minDepth(root: Optional[TreeNode]) -> int:
    depth = 0
    if not root:
        return depth

    q = collections.deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:
            break
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return depth
