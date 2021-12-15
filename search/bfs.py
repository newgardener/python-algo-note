from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        bfs_path.append(v)
        # 뽑힌 노드와 연결되었지만 아직 방문하지 않은 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




bfs_path = []
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * (len(graph))
bfs(graph, 1, visited)
print(bfs_path)