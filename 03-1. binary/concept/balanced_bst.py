class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalancedBST:
    def depth(self, node):
        if not node:
            return 0

        leftDepth = self.depth(node.left)
        if leftDepth == -1:
            return -1

        rightDepth = self.depth(node.right)
        if rightDepth == -1:
            return -1

        if abs(leftDepth - rightDepth) > 1:
            return -1

        return 1 + max(leftDepth, rightDepth)

    def isBalanced(self, root):
        return self.depth(root) != -1
