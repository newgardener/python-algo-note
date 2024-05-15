class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
        self.wordDict = WordDictionary.Node()

    def addWord(self, word: str) -> None:
        node = self.wordDict
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary.Node()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.wordDict

        for ch in word:
            if ch != "." and ch not in node.children:
                return False
            if ch == ".":
                keys = list(node.children.keys())
                if len(keys) == 0:
                    return False
                node = node.children[keys[0]]
            else:
                node = node.children[ch]
        return node.isEnd or word[-1] == "."


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
