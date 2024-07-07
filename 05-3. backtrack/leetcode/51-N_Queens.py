from typing import List

"""
Time Complexity:
- isValid: O(N) + O(N) + O(N) = O(N)
- dfs: O(N^n) 
=> O(N^n * N) = (N^(n+1))
"""


# %%


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


# %%
"""
Time Complexity:
- isValid: O(1)
- dfs: O(N^n)
=> O(N^n)
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        vertical = set()
        rightDiagonal = set()
        leftDiagonal = set()

        def isValid(row, col):
            return col not in vertical and (row + col) not in rightDiagonal and (row - col) not in leftDiagonal

        def dfs(row, board):
            if row >= n:
                solution = []
                for i in range(n):
                    solution.append("".join(board[i]))
                result.append(solution)
                return
            for col in range(n):
                if not isValid(row, col):
                    continue

                board[row][col] = "Q"
                vertical.add(col)
                rightDiagonal.add(row + col)
                leftDiagonal.add(row - col)
                dfs(row + 1, board)
                vertical.remove(col)
                rightDiagonal.remove(row + col)
                leftDiagonal.remove(row - col)
                board[row][col] = "."

        dfs(0, board)
        return result
