class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def findMin(self, node):
        if not node.left:
            return node
        return self.findMin(node.left)

    def insert(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            parent = None  # set parentNode
            while current is not None:
                parent = current
                if data < parent.data:
                    current = current.left
                else:
                    current = current.right

            if data < parent.data:
                parent.left = newNode
            else:
                parent.right = newNode

    def deleteNode(self, root, value):
        # base condition
        if root is None:
            return root
        if value < root.data:
            return self.deleteNode(root.left, value)
        elif value > root.data:
            return self.deleteNode(root.right, value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.findMin(self.right)
            root.data = temp.data
            root.right = self.deleteNode(root.right, temp)
        return root

    def delete(self, value):
        self.root = self.deleteNode(self.root, value)

    def search(self, node):
        current = self.root
        while current is not None:
            if current.data == node.data:
                return True
            elif node.data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inOrderHelper(self, node):
        if node is not None:
            self.inOrderHelper(node.left)
            print(node.data, end=" ")
            self.inOrderHelper(node.right)

    def inOrder(self):
        self.inOrderHelper(self.root)
        print()

    def preOrderHelper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preOrderHelper(node.left)
            self.preOrderHelper(node.right)

    def preOrder(self):
        self.preOrderHelper(self.root)
        print()

    def postOrderHelper(self, node):
        if node is not None:
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            print(node.data, end=" ")

    def postOrder(self):
        self.postOrderHelper(self.root)
        print()


if __name__ == "__main__":
    node = BST()
    node.insert(5)
    node.insert(3)
    node.insert(7)
    node.insert(2)
    node.insert(4)
    node.insert(6)
    node.insert(8)

    node.inOrder()
    node.preOrder()
    node.postOrder()

    node.delete(2)

    node.inOrder()
