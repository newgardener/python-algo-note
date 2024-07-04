from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeafNode(node):
    return node and not node.left and not node.right


def restorePath(root, leaf, parent):
    path = []
    while leaf != root:
        path.append(str(leaf.val))
        leaf = parent[leaf]
    path.append(str(root.val))
    return "".join(path[::-1])


def bfs(start):
    parent = dict()
    leaf = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if isLeafNode(node):
            leaf.append(node)
            continue
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)
    return leaf, parent
