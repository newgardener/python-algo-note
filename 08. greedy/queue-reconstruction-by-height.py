# %% solution 1

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

people.sort(key=lambda x: x[0], reverse=True)
result = []

for person in people:
    result.insert(person[1], person)

print(result)

# %% solution 2 - using heap (priority queue)
import heapq

heap = []

for person in people:
    heapq.heappush(heap, (-person[0], person[1]))

result = []
while heap:
    person = heapq.heappop(heap)
    result.insert(person[1], [-person[0], person[1]])

print(result)
