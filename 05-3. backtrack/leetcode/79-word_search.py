from typing import List


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
