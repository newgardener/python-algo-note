def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0])
    l, r = 0, n - 1
    t, d = 0, m - 1
    turn = "R"  # 'R' (right), 'D' (down), 'L' (left), 'U' (up)
    res = []
    while l <= r and t <= d:
        if turn == "R":
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            turn = "D"
        elif turn == "D":
            for i in range(t, d + 1):
                res.append(matrix[i][r])
            r -= 1
            turn = "L"
        elif turn == "L":
            for i in range(r, l - 1, -1):
                res.append(matrix[d][i])
            d -= 1
            turn = "U"
        else:
            for i in range(d, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            turn = "R"
    return res
