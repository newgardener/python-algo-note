import collections
from typing import List

"""
Time Complexity: O(9^2)
check all rows, cols, squares whether it only contains 1-9 once
"""


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num == ".":
                continue

            if num in rows[i] or num in cols[j] or num in squares[(i // 3, j // 3)]:
                return False

            rows[i].add(num)
            cols[j].add(num)
            squares[(i // 3, j // 3)].add(num)

    return True
