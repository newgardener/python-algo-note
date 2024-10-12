def matrixScore(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    for r in range(m):
        if grid[r][0] == 0:
            for c in range(n):
                # xor each item to flip value (0 -> 1, 1 -> 0)
                grid[r][c] ^= 1

    for c in range(n):
        ones = sum(grid[r][c] for r in range(m))
        if ones < m / 2:
            for r in range(m):
                grid[r][c] ^= 1

    # sum each row of bits as a binary value
    return sum(int("".join(map(str, row)), 2) for row in grid)
