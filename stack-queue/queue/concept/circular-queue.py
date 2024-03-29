class CircularQueue:
    def __init__(self, size):
        self.size = size + 1
        self.queue = [None] * size
        self.front = self.rear = 0
        
    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue is full')
        
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        
        item = self.queue[self.front]
        self.queue[self.front] = None # clear the vacated spot
        self.front = (self.front + 1) % self.size
        return item 
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def size(self):
        return (self.rear - self.front + self.size) % self.size
    
    def displayQueue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        print("Elements in the Circular Queue are: ")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size + 1):
                print(self.queue[i], end="")

if __name__ == '__main__':
    q = CircularQueue(5)        

    q.enqueue(14)
    q.enqueue(22)
    q.enqueue(13)
    q.enqueue(-6)

    q.displayQueue()

    print("Deleted value =", q.dequeue())
    print("Deleted value =", q.dequeue())

    q.displayQueue()



