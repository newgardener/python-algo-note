import heapq


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    # weight between node u and node v
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def primsMst(self):
        mst = []
        total_cost = 0

        # (cost, vertex) in order to extract smallest cost one at a time
        min_heap = [(0, 0)]
        visited = set()

        while min_heap:
            cost, u = heapq.heappop(min_heap)

            if u in visited:
                continue

            visited.add(u)
            total_cost += cost
            mst.append((u, cost))

            for v, weight in self.graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))

        return mst, total_cost


graph = Graph(5)
graph.addEdge(0, 1, 10)
graph.addEdge(0, 3, 5)
graph.addEdge(1, 2, 1)
graph.addEdge(1, 3, 2)
graph.addEdge(2, 3, 9)
graph.addEdge(2, 4, 4)
graph.addEdge(3, 4, 7)


mst, total_cost = graph.primsMst()
print(mst, total_cost)
