class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        start, result = 0, 0

        while start < len(s):
            curr = trie.root
            longest_match = -1

            for i in range(start, len(s)):
                ch = s[i]
                if ch not in curr.children:
                    break
                curr = curr.children[ch]
                if curr.isEnd:
                    longest_match = i

            if longest_match == -1:
                result += 1
                start += 1
            else:
                start = longest_match + 1

        return result
