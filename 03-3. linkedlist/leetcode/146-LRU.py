from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.queue = deque([])

    def get(self, key: int) -> int:
        if key in self.hashmap:
            value = self.hashmap[key]
            while len(self.queue) >= self.capacity:
                pk, pv = self.queue.popleft()
            self.queue.append((key, value))
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        while len(self.queue) >= self.capacity:
            if key in self.hashmap:
                break
            pk, pv = self.queue.popleft()
            if pk in self.hashmap:
                del self.hashmap[pk]
        if key not in self.hashmap:
            self.queue.append((key, value))
        self.hashmap[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
