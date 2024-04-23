def numIslands(grid: list[list[str]]) -> int:
    def dfs(row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

    m, n = len(grid), len(grid[0])

    island = 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "1":
                dfs(row, col)
                island += 1

    return island


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(numIslands(grid))
