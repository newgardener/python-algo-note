# https://leetcode.com/problems/find-all-groups-of-farmland

# %%
from collections import deque


def findFarmlandBFS(land: list[list[int]]) -> list[list[int]]:
    def bfs(i, j, visited):
        queue = deque([(i, j)])
        visited.add((i, j))
        r1, c1, r2, c2 = i, j, i, j

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
                    continue
                if (nx, ny) in visited or land[nx][ny] == 0:
                    continue
                queue.append((nx, ny))
                # should add to visited when enqueueing in order to add a cell once
                visited.add((nx, ny))
                r2, c2 = max(nx, r2), max(ny, c2)
        return r1, c1, r2, c2

    visited = set()
    result = []
    for i in range(len(land)):
        for j in range(len(land[0])):
            if (i, j) not in visited and land[i][j] == 1:
                r1, c1, r2, c2 = bfs(i, j, visited)
                result.append([r1, c1, r2, c2])
    return result


# %%
def findFarmland(land: list[list[int]]) -> list[list[int]]:
    m, n = len(land), len(land[0])

    result = []
    for i in range(m):
        for j in range(n):
            # travel only (0, 1), (1, 0) directions
            # condition to avoid traveling visited cells again
            if (
                land[i][j] == 0
                or (j > 0 and land[i][j - 1] == 1)
                or (i > 0 and land[i - 1][j] == 1)
            ):
                continue
            r2, c2 = i, j
            while r2 + 1 < m and land[r2 + 1][j] == 1:
                r2 += 1
            while c2 + 1 < n and land[i][c2 + 1] == 1:
                c2 += 1
            result.append([i, j, r2, c2])
    return result
