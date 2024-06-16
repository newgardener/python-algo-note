# %%
from collections import defaultdict
from operator import le, ne


class UnOptimizedSolution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        def findTreeHeight(node, visited, current_depth=1):
            visited.add(node)

            max_depth = current_depth

            for vertex in graph[node]:
                if vertex not in visited:
                    child_depth = findTreeHeight(vertex, visited, current_depth + 1)
                    max_depth = max(max_depth, child_depth)

            return max_depth

        if n == 1:
            return [0]

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        min_height = float("inf")
        result = []
        for node in range(n):
            height = findTreeHeight(node, set())
            result.append((node, height))
            min_height = min(min_height, height)

        return list(map(lambda x: x[0], filter(lambda x: x[1] == min_height, result)))


# %%
# pass only odd number path
from collections import defaultdict, deque


class OptimizedIntermediateSolution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            visited = [-1] * n
            visited[start] = 0
            queue = deque([start])
            farthest_node = start

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        queue.append(neighbor)
                        visited[neighbor] = visited[node] + 1
                        if visited[neighbor] > visited[farthest_node]:
                            farthest_node = neighbor
            return farthest_node, visited

        # First BFS to find one end of the diameter
        farthest, _ = bfs(0)
        # Second BFS to find the actual diameter and distances
        farthest, distances = bfs(farthest)

        min_height = float("inf")
        for distance in distances:
            if distance == 0:
                continue
            min_height = min(min_height, distance)

        return [i for i in range(n) if distances[i] == min_height]


# %%
# pass both odd and even number path
from collections import defaultdict, deque


class OptimizedSolution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            parent = [-1] * n
            visited = [-1] * n
            visited[start] = 0
            queue = deque([start])
            farthest_node = start

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        queue.append(neighbor)
                        parent[neighbor] = node
                        visited[neighbor] = visited[node] + 1
                        if visited[neighbor] > visited[farthest_node]:
                            farthest_node = neighbor

            max_distance = max(visited)
            farthest_node = visited.index(max_distance)
            return farthest_node, visited, parent

        # First BFS to find one end of the diameter
        farthest, _, _ = bfs(0)
        # Second BFS to find the actual diameter and distances
        farthest, distances, parent = bfs(farthest)

        path = []
        while farthest != -1:
            path.append(farthest)
            farthest = parent[farthest]

        length = len(path)
        if length % 2 == 0:
            return [path[length // 2 - 1], path[length // 2]]
        else:
            return [path[length // 2]]


# %%
n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]


# answer = UnOptimizedSolution().findMinHeightTrees(n, edges)
# answer = UnOptimizedIntermediateSolution().findMinHeightTrees(n, edges)
answer = OptimizedSolution().findMinHeightTrees(n, edges)
print(answer)
