from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    grids = defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num in rows[i] or num in cols[j] or num in grids[(i // 3, j // 3)]:
                return False

            rows[i].add(num)
            cols[j].add(num)
            grids[(i // 3, j // 3)].add(num)

    return True
