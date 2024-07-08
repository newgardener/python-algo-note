class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, dict):
        node = self.root
        acc = ""
        for ch in word:
            acc += ch
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if acc not in dict:
                dict[acc] = []
            dict[acc].append(word)
        node.isEnd = True


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        dict = {}
        trie = Trie()
        for product in products:
            trie.insert(product, dict)

        result = []
        for i in range(len(searchWord)):
            word = searchWord[: i + 1]
            suggests = sorted(dict.get(word, []))[:3]
            result.append(suggests)
        return result


solution = Solution()

products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(solution.suggestedProducts(products, searchWord))
