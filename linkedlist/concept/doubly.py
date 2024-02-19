class DLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DLNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node  # newly added node to be head

    def insert_after(self, prev_node, data):
        if prev_node is None:
            raise Exception("prev_node should be in the linked list")

        new_node = DLNode(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node  # update prev of prev_node which would be placed after new_node

    def delete(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            temp = temp.next

        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        temp = None  # free memory

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    dllist = DoublyLinkedList()

    dllist.insert(1)
    dllist.insert(2)
    dllist.insert(3)

    print("Search 2:", dllist.search(2))  # True
    dllist.delete(2)
    print("Search 2:", dllist.search(2))  # False
