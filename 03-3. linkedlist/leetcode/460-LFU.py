from collections import OrderedDict, defaultdict

"""
TODO: should implement LinkedList (length, pop, popLeft, pushRight) on your own and use those methods to implement LFUCache
"""


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu = 0
        self.cache = dict()  # key-node
        self.freq = defaultdict(OrderedDict)  # count-(key-node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int):
        if self.capacity == 0:
            return

        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                k, v = self.freq[self.lfu].popitem(last=False)
                self.cache.pop(k)
            node = ListNode(key, value)
            self.cache[key] = node
            self.freq[1][key] = value
            self.lfu = 1
        else:
            node = self.cache[key]
            node.val = value
            self.update(node)

    def update(self, node):
        k, v, f = node.key, node.val, node.freq
        self.freq[f].pop(k)
        if not self.freq[f] and self.lfu == f:
            self.lfu += 1
        self.freq[f + 1][k] = v
        node.freq += 1
