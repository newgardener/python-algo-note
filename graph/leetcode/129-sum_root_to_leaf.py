from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root: optional[TreeNode]) -> int:
    def isLeafNode(node):
        return node and not node.left and not node.right

    def restorePath(leaf, parents):
        path = []
        while leaf != root:
            path.append(str(leaf.val))
            leaf = parents[leaf]
        path.append(str(root.val))
        return "".join(path[::-1])

    def bfs(start):
        parents = {}
        leafNodes = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if isLeafNode(node):
                leafNodes.append(node)
                continue
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
        return leafNodes, parents

    leafNodes, parents = bfs(root)

    result = 0
    for leaf in leafNodes:
        result += int(restorePath(leaf, parents))
    return result
