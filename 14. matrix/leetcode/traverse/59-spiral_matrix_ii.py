def generateMatrix(n: int) -> list[list[int]]:
    l, r = 0, n - 1
    t, d = 0, n - 1
    matrix = [[0] * n for _ in range(n)]
    turn = "R"  # 'R' (right) 'D' (down) 'L' (left) 'U' (up)
    n = 1
    while l <= r and t <= d:
        if turn == "R":
            for i in range(l, r + 1):
                matrix[t][i] = n
                n += 1
            t += 1
            turn = "D"
        elif turn == "D":
            for i in range(t, d + 1):
                matrix[i][r] = n
                n += 1
            r -= 1
            turn = "L"
        elif turn == "L":
            for i in range(r, l - 1, -1):
                matrix[d][i] = n
                n += 1
            d -= 1
            turn = "U"
        else:
            for i in range(d, t - 1, -1):
                matrix[i][l] = n
                n += 1
            l += 1
            turn = "R"

    return matrix
