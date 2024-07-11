"""
Take-Away:
Q. passing the remaining part of the word or passing the current index, which is better?
   search(node, word[1:]) or search(node, i+1)
A. In terms of Space Complexity,
M = length of the word
- passing the remaining part: O(M^2)
- passing the index: O(M)
When creating a recursion, index-based approach is better in terms of memory efficiency
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


# %%

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addNode(self, word: str) -> None:
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def _search(self, node, word):
        # base case
        if not word:
            return node.isEnd

        ch = word[0]
        if ch == '.':
            return any(self._search(node, word[1:]) for node in node.children.values())
        else:
            if ch not in node.children:
                return False
            return self._search(node.children[ch], word[1:])

    def search(self, word: str) -> bool:
        return self._search(self.root, word)


# %%


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            ch = word[i]
            if ch == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)
