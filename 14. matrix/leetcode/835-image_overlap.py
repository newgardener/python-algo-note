from collections import defaultdict


def largestOverlap(img1: list[list[int]], img2: list[list[int]]) -> int:
    n = len(img1)
    ones1, ones2 = [], []
    for i in range(n):
        for j in range(n):
            if img1[i][j] == 1:
                ones1.append((i, j))
            if img2[i][j] == 1:
                ones2.append((i, j))

    d = defaultdict(int)
    # check diff between (r1, c1) and (r2, c2)
    for r1, c1 in ones1:
        for r2, c2 in ones2:
            d[(r2 - r1, c2 - c1)] += 1
    return max(d.values() or [0])
