from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def addWord(self, root, words: List[str]):
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        result = []

        # add words to a trie
        self.addWord(root, words)

        def dfs(r, c, node, path):
            # out of bound or already visited
            if r >= m or r < 0 or c >= n or c < 0 or board[r][c] == '#':
                return False

            ch = board[r][c]
            if ch not in node.children:
                return False
            nextNode = node.children[ch]
            # found a word
            # NOTICE: should not return after finding a word!
            # because there would be longer words containing the found word as a prefix
            if nextNode.word:
                result.append(nextNode.word)
                nextNode.word = None

            original = board[r][c]
            board[r][c] = '#'
            dfs(r - 1, c, nextNode, path + board[r][c])
            dfs(r + 1, c, nextNode, path + board[r][c])
            dfs(r, c - 1, nextNode, path + board[r][c])
            dfs(r, c + 1, nextNode, path + board[r][c])
            board[r][c] = original

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, '')
        return result
