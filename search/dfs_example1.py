#%% 음료수 얼려먹기

n, m = map(int, input().split())

# 2차원 리스트 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 현재 노드가 아직 방문되지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우 모두 재귀 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
            
print(result)



