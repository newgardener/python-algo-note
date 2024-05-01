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
