# %%
from collections import defaultdict


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


n = 4
edges = [[1, 0], [1, 2], [1, 3]]

answer = UnOptimizedSolution().findMinHeightTrees(n, edges)
print(answer)
