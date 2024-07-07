from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        def isValid(row, col, board):
            # check column
            for i in range(n):
                if board[i][col] == "Q":
                    return False
            # check upper right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            # check upper left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            return True

        def dfs(row, board):
            if row >= n:
                solution = []
                for i in range(n):
                    solution.append("".join(board[i]))
                result.append(solution)
                return
            for col in range(n):
                if not isValid(row, col, board):
                    continue
                board[row][col] = "Q"
                dfs(row + 1, board)
                board[row][col] = "."

        dfs(0, board)
        return result
