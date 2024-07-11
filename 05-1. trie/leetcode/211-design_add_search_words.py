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
            def dfs(i, node):
                curr = node
                for j in range(i, len(word)):
                    ch = word[j]
                    if ch == ".":
                        for child in curr.children.values():
                            if dfs(j + 1, child):
                                return True
                        return False
                    else:
                        if ch not in curr.children:
                            return False
                        curr = curr.children[ch]
                return curr.isEnd

            return dfs(0, self.root)

    # Your WordDictionary object will be instantiated and called as such:
    # obj = WordDictionary()
    # obj.addWord(word)
    # param_2 = obj.search(word)
