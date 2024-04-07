class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def closestValue(root: TreeNode, target: float) -> int:
    closest_value = root.val

    while root:
        if abs(target - root.val) < abs(target - closest_value):
            closest_value = root.val

        if target < root.val:
            root = root.left
        else:
            root = root.right

    return closest_value


if __name__ == "__main__":
    example = TreeNode(5)
    example.left = TreeNode(3)
    example.left.left = TreeNode(1)
    example.left.right = TreeNode(4)
    example.right = TreeNode(8)
    example.right.left = TreeNode(6)
    example.right.right = TreeNode(9)

    print(closestValue(example, 6.4))
