# %%
def islandPerimeterDfs(grid: list[list[int]]) -> int:
    self.n, self.m = len(grid), len(grid[0])
    self.visited = set()

    def dfs(i, j, perimeter=0):
        if (i, j) in self.visited:
            return perimeter

        if i < 0 or i > self.n or j < 0 or j > self.m or grid[i][j] == 0:
            return perimeter + 1

        self.visited.add((i, j))
        return (
            dfs(i - 1, j, perimeter)
            + dfs(i + 1, j, perimeter)
            + dfs(i, j - 1, perimeter)
            + dfs(i, j + 1, perimeter)
        )

    for i in range(self.n):
        for j in range(self.m):
            if grid[i][j] == 1 and (i, j) not in self.visited:
                return dfs(i, j, 0)


# %%
def islandPerimeter(grid: list[list[int]]) -> int:
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if (
                        ni < 0
                        or nj < 0
                        or ni >= rows
                        or nj >= cols
                        or grid[ni][nj] == 0
                    ):
                        perimeter += 1
    return perimeter
