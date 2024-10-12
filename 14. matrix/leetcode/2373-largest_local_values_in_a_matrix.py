# apply 3x3 filter consecutively on the grid to find localMax of each turn
def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    matrix = []
    for r in range(n - 2):
        row = []
        for c in range(n - 2):
            localMax = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    localMax = max(localMax, grid[i][j])
            row.append(localMax)
        matrix.append(row)
    return matrix
