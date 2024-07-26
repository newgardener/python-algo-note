from collections import defaultdict
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        intervals.sort(key=lambda x: x[0])
        size = [item[1] - item[0] + 1 for item in intervals]

        def process(query):
            # find leftmost interval
            left, right = 0, len(intervals) - 1
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][1] < query:
                    left = mid + 1
                else:
                    right = mid - 1

            minSize = float('infinity')
            for i in range(left, n):
                start, end = intervals[i]
                if start > query:
                    break
                if start <= query <= end:
                    minSize = min(minSize, size[i])
            return minSize if minSize != float('infinity') else -1

        return [process(q) for q in queries]
