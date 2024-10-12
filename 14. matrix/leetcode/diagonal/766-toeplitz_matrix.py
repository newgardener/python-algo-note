from collections import deque


def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    expected = deque(matrix[0])

    for r in range(1, len(matrix)):
        row = matrix[r]
        expected.pop()
        expected.appendleft(row[0])

        # check if diagonal values are the same
        for c in range(1, len(row)):
            if row[c] != expected[c]:
                return False

    # validated to have all the same values in top-left to bottom-right diagonals
    return True
