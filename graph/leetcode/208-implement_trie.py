# https://leetcode.com/problems/implement-trie-prefix-tree

"""
n - number of inserted keys, m - key length or average key length
Time Complexity:
  - Insert: O(m)
  - Search and StartsWith: O(m)
Space Complexity: O(n*m)
"""


class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie.Node()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
