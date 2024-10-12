# transpose matrix (r, c) -> (c, r)
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    m, n = len(matrix), len(matrix[0])
    T = [[0] * m for _ in range(n)]
    for r in range(m):
        for c in range(n):
            T[c][r] = matrix[r][c]
    return T
