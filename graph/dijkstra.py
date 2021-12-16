import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 출발 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 테이블
graph = [[] for i in range(n+1)]
# 최단거리 테이블 INF로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # 노드 a -> 노드 b로 가는 비용 == c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for n_node, n_dist in graph[now]:
            cost = dist + n_dist
            if cost < distance[n_node]:
                distance[n_node] = cost
                heapq.heappush(q, (cost, n_node))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


            




