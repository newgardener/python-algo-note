from queue import Queue

class Solution:
    def __init__(self):
        self.main = Queue()
        self.aux = Queue()
    
    def push(self, val):
        self.aux.put(val)
        while not self.main.empty():
            self.aux.put(self.main.get())

        self.main,self.aux = self.aux,self.main
    
    def pop(self):
        return self.main.get()
    
    def get_queue_elements(self, queue):
        elements = []
        size = queue.qsize()
        
        for _ in range(size):
            element = queue.get()
            elements.append(element)
            queue.put(element)
            
        return elements
    
    def visualize_queues(self):
        print('Main Queue >>>')
        for main_element in self.get_queue_elements(self.main):
            print(main_element, end=' ')
        
        print('\nAux Queue >>>')
        for aux_element in self.get_queue_elements(self.aux):
            print(aux_element, end=' ')
            
if __name__ == '__main__':
    stack = Solution()

    stack.push(1)
    stack.visualize_queues()
    stack.push(2)
    stack.visualize_queues()
    stack.push(3)
    stack.visualize_queues()
    
    







