import heapq


def connectSticks(sticks):
    cost = 0

    min_heap = sticks[:]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        num = 0
        num += heapq.heappop(min_heap)
        num += heapq.heappop(min_heap)
        cost += num
        heapq.heappush(min_heap, num)

    return cost


if __name__ == "__main__":
    print(connectSticks([1, 1, 1, 1]))
