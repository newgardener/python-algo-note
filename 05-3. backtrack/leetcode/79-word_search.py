from typing import List

"""
l = length of word, 4 directions (up, down, left, right)
Time Complexity: (m * n * 4^l)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()

        def isBounded(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if not isBounded(r, c) or (r, c) in visited or board[r][c] != word[idx]:
                return False

            visited.add((r, c))
            res = dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1) or dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1)
            visited.remove((r, c))
            return res

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
