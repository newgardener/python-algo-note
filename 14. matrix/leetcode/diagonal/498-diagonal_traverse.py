from collections import defaultdict


def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    m, n = len(mat), len(mat[0])
    d = defaultdict(list)
    for r in range(m):
        for c in range(n):
            d[r + c].append(mat[r][c])

    res = []
    for k, v in d.items():
        if k % 2 == 0:
            res.extend(v[::-1])
        else:
            res.extend(v)
    return res
