class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)

        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        if self.get_size() == 1:
            self.front = None
        else:
            tmp_node = self.front
            first_node = self.front.next
            self.front = first_node
            if self.front is None:
                self.rear = None

        self.size -= 1
        return tmp_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def is_empty(self):
        return self.front == None

    def get_size(self):
        return self.size


if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display front element
    print("Front element:", queue.peek())
    # Dequeue and display the dequeued element
    print("Dequeued:", queue.dequeue())
    # Display front element again
    print("Front element:", queue.peek())
    # Display the size of the queue
    print("Queue size:", queue.get_size())
