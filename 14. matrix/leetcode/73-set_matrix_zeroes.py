def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeroes = []
    m, n = len(matrix), len(matrix[0])
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zeroes.append((r, c))

    # turn row and col which includes (r, c) all zeroes
    for r, c in zeroes:
        for i in range(m):
            matrix[i][c] = 0
        for j in range(n):
            matrix[r][j] = 0



