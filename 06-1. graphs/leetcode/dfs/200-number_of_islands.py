"""
https://leetcode.com/problems/number-of-islands/description/
"""


def numIslands(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(row, col):
        grid[row][col] = '0'
        for nr, nc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                dfs(nr, nc)

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
