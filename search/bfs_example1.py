from collections import deque

n, m = map(int, input().split())

# 2차원 리스트 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            # 미로 찾기 경계에서 벗어날 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))