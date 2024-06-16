from collections import deque
import copy

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for v in info[1:-1]:
        indegree[i] += 1
        graph[v].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result


result = topology_sort()
print(result)
