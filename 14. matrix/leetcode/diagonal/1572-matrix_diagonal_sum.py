def diagonalSum(mat: list[list[int]]) -> int:
    n = len(mat)
    res = 0
    for i in range(n):
        res += mat[i][i]
    col = n - 1
    for j in range(n):
        res += mat[j][col]
        col -= 1

    # diagonals of odd-length matrix intersect in the middle
    if n % 2 == 1:
        return res - mat[n // 2][n // 2]
    return res
