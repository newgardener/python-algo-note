from typing import List

# %%
"""
Problem: we don't need to hold all characters in the path  
Solution: increment word index by 1 and if word index reaches the word length, it means we found it!
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def isBounded(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(pos, path):
            i, j = pos
            pathWord = ''.join(path)

            if pathWord != word[:len(path)]:
                return False

            if pathWord == word:
                return True

            visited.add((i, j))

            for dx, dy in dirs:
                newPos = (i + dx, j + dy)
                if isBounded(*newPos) and newPos not in visited:
                    if dfs(newPos, path + [board[dx][dy]]):
                        return True

            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs((i, j), [word[0]]):
                        return True
        return False


# %%

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
