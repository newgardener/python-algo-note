class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1

    newNode = TreeNode(t1.val + t2.val)
    newNode.left = mergeTrees(t1.left, t2.left)
    newNode.right = mergeTrees(t1.right, t2.right)

    return newNode


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(5)

    mergeTrees(tree1, tree2)
