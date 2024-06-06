from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for i in range(3):
        for j in range(3):
            grid = [
                [(i * 3 + x, j * 3), (i * 3 + x, j * 3 + 1), (i * 3 + x, j * 3 + 2)]
                for x in range(3)
            ]
            numSet = set()
            for coords in grid:
                for coord in coords:
                    num = board[coord[0]][coord[1]]
                    if num == ".":
                        continue
                    if num in numSet:
                        return False
                    numSet.add(num)
        return True
