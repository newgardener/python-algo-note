# %% heapq

import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        # 오름차순 정렬
        heapq.heappush(h, value)
        # 내림차순 정렬
        # heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# %% heapify
import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

heapq.heapify(nums)
for _ in range(len(nums) - k):
    heapq.heappop(nums)
print(heapq.heappop(nums))  # Kth largest num

# %% nlargest
import heapq

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

print(heapq.nlargest(k, nums)[-1])
print(heapq.nsmallest(k, nums)[-1])

# %% Priority Queue
import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


pq = PriorityQueue()
pq.push("task1", priority=3)
pq.push("task2", priority=1)
pq.push("task3", priority=2)
pq.push("task4", priority=3)

print(pq)
print(pq.pop())  # task1 (highest priority)
print(pq.pop())  # task4
print(pq.pop())  # task3
print(pq.pop())  # task2


# %% Dijikstra's algorithm
import heapq

graph = {
    "A": [("B", 1), ("D", 4)],
    "B": [("A", 1), ("C", 2), ("E", 3)],
    "C": [("B", 2), ("F", 1)],
    "D": [("A", 4), ("E", 5)],
    "E": [("B", 3), ("D", 5), ("F", 2)],
    "F": [("C", 1), ("E", 2)],
}


def dijikstra(graph, start):
    pq = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # if the popped distance is greater than the recorded, skip the node
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


dijikstra(graph, "A")


# %% Prim's algorithm
import heapq

graph = {
    "A": [("B", 1), ("C", 3), ("D", 4)],
    "B": [("A", 1), ("C", 2)],
    "C": [("A", 3), ("B", 2), ("D", 5)],
    "D": [("A", 4), ("C", 5)],
    "E": [("C", 6), ("D", 6)],
}


def prims_algorithm(graph, start):
    pq = [(0, start, None)]  # (weight, target vertex, source vertex)
    mst = []
    total_weight = 0
    visited = set()

    while pq:
        weight, vertex, src = heapq.heappop(pq)
        if vertex in visited:
            continue  # skip if already visited

        visited.add(vertex)
        if src is not None:  # in order not to add starting vertex
            mst.append((src, vertex, weight))
            total_weight += weight

        # add all edges from this vertex to the priority queue
        for next_vertex, next_weight in graph[vertex]:
            if next_vertex not in visited:
                heapq.heappush(pq, (next_weight, next_vertex, vertex))

    return mst, total_weight


mst, total_weight = prims_algorithm(graph, "A")
print("MST:", mst)
print("total weight:", total_weight)
