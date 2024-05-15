from collections import deque, defaultdict


class DAG:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1
        if u not in self.in_degree:
            self.in_degree[u] = 0

    def topology_sort(self):
        queue = deque([node for node in self.in_degree if self.in_degree[node] == 0])
        sorted_list = []

        while queue:
            u = queue.popleft()
            sorted_list.append(u)
            for v in self.graph[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)

        if len(sorted_list) != len(self.in_degree):
            raise Exception("The graph has at least one cycle")

        return sorted_list
