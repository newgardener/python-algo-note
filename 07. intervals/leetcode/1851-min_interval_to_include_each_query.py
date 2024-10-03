import heapq


def minInterval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    # sort intervals by its startTime
    intervals.sort()
    sizes = [r - l + 1 for l, r in intervals]

    minHeap = []
    res = {}
    i = 0
    for q in sorted(queries):
        # if startTime of intervals[i] is smaller or equal to q, we can insert to minHeap
        # minHeap manages (size, endTime of interval) to pop the smallest possible interval
        while i < len(intervals) and intervals[i][0] <= q:
            heapq.heappush(minHeap, (sizes[i], intervals[i][1]))
            i += 1

        # pop all invalid intervals where endTime is smaller than q
        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)

        res[q] = minHeap[0][0] if minHeap else -1

    return [res[q] for q in queries]
