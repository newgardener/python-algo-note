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

#%% letter combinations

digits = "23"

def dfs(index, path):
    if len(path) == len(digits):
        result.append(path)
        return
    
    for i in range(index, len(digits)):
        for j in dic[digits[i]]:
            dfs(i+1, path+j)

if not digits:
    print("None")

dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8':' tuv', '9': 'wxyz'}
result = []
dfs(0, "")
print(result)



# %% combinations

# 전체 수 1~4 중 2개의 조합 생성 
n = 4
k = 2

def combine(n, k):
    result = []

    def dfs(elements, start, k):
        if k == 0:
            result.append(elements[:])
            return
        
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
    
    dfs([], 1, k)
    return result

combine(n, k)
    

# %%
