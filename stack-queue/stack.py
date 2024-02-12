# %% Stack Implementation using an array


class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        if self.top == len(self.stack) - 1:
            raise Exception("Stack is full")

        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")

        data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1


# %% Stack Implementation using a linked list

"""
pros compared to the array-based implementation above
- dynamically-sized
- avoid overflow issue in array
"""


class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, item):
        node = self.Node(item)
        node.next = self.top
        self.top = node  # update the top to a new node

    def pop(self):
        if self.isEmpty():
            raise Exception("pop from empty stack")

        item = self.top.data
        self.top = self.top.next  # update the top to the next node
        return item

    def peek(self):
        if self.isEmpty():
            raise Exception("peek from empty stack")

        return self.top.data

    def isEmpty(self):
        return self.top == None
