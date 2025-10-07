from typing import List

"""
Time Complexity:
- isValid: O(N) + O(N) + O(N) = O(N)
- dfs: O(N!) 
=> O(N! * N) = O(N!)
"""


# %%


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        def isValid(row, col):
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

        def dfs(row):
            if row >= n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if not isValid(row, col):
                    continue
                board[row][col] = "Q"
                dfs(row + 1)
                board[row][col] = "."

        dfs(0)
        return result


# %%
"""
Time Complexity:
- isValid: O(1)
- dfs: O(N!)
=> O(N!)
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        rightDiag = set()
        leftDiag = set()

        def isValid(row, col):
            return col not in cols and (row + col) not in rightDiag and (row - col) not in leftDiag

        def dfs(row):
            if row >= n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if not isValid(row, col):
                    continue

                # Place Queen
                board[row][col] = "Q"
                cols.add(col)
                rightDiag.add(row + col)
                leftDiag.add(row - col)

                dfs(row + 1)

                # Backtrack
                cols.remove(col)
                rightDiag.remove(row + col)
                leftDiag.remove(row - col)
                board[row][col] = "."

        dfs(0)
        return result
