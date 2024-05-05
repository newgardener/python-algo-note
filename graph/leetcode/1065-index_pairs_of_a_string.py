class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True  # mark the end of a word


class Solution:
    def indexPairs(self, text, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = []
        for i in range(len(text)):
            node = trie.root
            for j in range(i, len(text)):
                ch = text[j]
                # character is not in a trie
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.isEnd:
                    result.append([i, j])
        return result


solution = Solution()

text1 = "bluebirdskyscraper"
words1 = ["blue", "bird", "sky"]
print(solution.indexPairs(text1, words1))

text2 = "programmingisfun"
words2 = ["pro", "is", "fun", "gram"]
print(solution.indexPairs(text2, words2))

text3 = "interstellar"
words3 = ["stellar", "star", "inter"]
print(solution.indexPairs(text3, words3))
