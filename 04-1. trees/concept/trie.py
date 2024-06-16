class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        # convert char to index (0-25)
        return ord(ch) - ord("a")

    def hasNoChild(self, children):
        return all(child is None for child in children)

    """
    Time Complexity: O(n) with n is the length of word
    Space Complexity: O(1) if best, O(n) if worst
       - worst case scenario when the word doesn't share any characters in the Trie
    """

    def insert(self, word):
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def search(self, word):
        node = self.root
        for char in word:
            index = self.charToIndex(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.isEndOfWord

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def _delete(self, current: TrieNode, word: str, index: int):
        if index == len(word):
            if current.isEndOfWord:
                current.isEndOfWord = False
                return self.hasNoChild(current.children)
            return False

        char = word[index]
        charIndex = self.charToIndex(char)
        node = current.children[charIndex]
        # word not exist case
        if not node:
            return False

        shouldDeleteChild = self._delete(node, word, index + 1)
        if shouldDeleteChild:
            current.children[charIndex] = None
            return self.hasNoChild(current.children) and not current.isEndOfWord
        return False

    def deleteWord(self, word):
        self._delete(self.root, word, 0)
