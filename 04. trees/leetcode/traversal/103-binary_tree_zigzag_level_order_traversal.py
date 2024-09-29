from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    res = []
    if not root:
        return res

    q = deque([(root, 1)]) # (node, level)
    while q:
        q_len = len(q)
        arr = []
        curr_level = 0
        for _ in range(q_len):
            node, curr_level = q.popleft()
            arr.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append((child, curr_level + 1))
        # zigzag traversal
        # left to right
        if curr_level % 2 == 1:
            res.append(arr)
        # right to left
        else:
            res.append(reversed(arr))

    return res
