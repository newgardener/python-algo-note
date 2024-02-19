class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            raise Exception("prev_node should be in the linked list")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, data):
        temp = self.head

        if temp is not None and temp.data == data:
            self.head = temp.next
            temp = None  # free memory
            return

        while temp is not None:
            if temp.data == data:
                break
            prev = temp  # save the prev node
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next
        temp = None  # free memory

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    sllist = SinglyLinkedList()

    sllist.insert(1)
    sllist.insert(2)
    sllist.insert(3)

    print("Search 2:", sllist.search(2))

    sllist.delete(2)

    print("Search 2:", sllist.search(2))
