# apply 3x3 filter consecutively on the grid to find localMax of each turn
def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    matrix = []
    r = 0
    while r + 3 <= n:
        row = []
        c = 0
        while c + 3 <= n:
            localMax = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    localMax = max(localMax, grid[i][j])
            row.append(localMax)
            c += 1
        matrix.append(row)
        r += 1
    return matrix
