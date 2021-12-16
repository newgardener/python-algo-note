"""

spanning tree = 모든 노드를 포함하면서 사이클이 존재 하지 않는 부분 그래프
minimum_spanning_tree 활용 사례
e.g. 모든 도시를 최소한의 비용으로 연결해야 할 때
적용한 알고리즘 = Kruskal algorithm
1) 간선 비용을 오름차순으로 정렬
2) 간선을 하나씩 확인하며 사이클 발생 여부를 확인 후, 
   사이클이 발생하지 않는 경우에만 포함시킴
3) 모든 간선에 대해 2)를 반복 
    
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


