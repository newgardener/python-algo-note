# https://leetcode.com/problems/extra-characters-in-a-string/description/


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
    def minExtraCharBackward(self, s: str, dictionary: list[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        n = len(s)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1

            node = trie.root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.isEnd:
                    dp[start] = min(dp[start], dp[end + 1])
        return dp[0]

    def minExtraCharForward(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        dp = [float("inf")] * (n + 1)
        words = set(dictionary)
        dp[0] = 0

        for i in range(1, n + 1):
            for word in words:
                j = len(word)
                if i >= j and s[i - j : i] == word:
                    dp[i] = min(dp[i], dp[i - j])
            dp[i] = min(dp[i], dp[i - 1] + 1)
        return dp[n]


solution = Solution()

s1 = "leetscode"
dictionary1 = ["leet", "code", "leetcode"]
print(solution.minExtraCharForward(s1, dictionary1))
print(solution.minExtraCharBackward(s1, dictionary1))

s2 = "sayhelloworld"
dictionary2 = ["hello", "world"]
print(solution.minExtraCharForward(s2, dictionary2))
print(solution.minExtraCharBackward(s2, dictionary2))
