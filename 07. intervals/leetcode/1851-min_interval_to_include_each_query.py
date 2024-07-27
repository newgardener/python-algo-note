from collections import defaultdict
from typing import List

"""
Why it is not working?
edge case found when 
intervals=[[6,6],[5,5],[10,10],[3,6],[9,9],[7,7],[2,10],[5,5],[3,7],[10,10]],
queries=[1,8,9,1,8,3,9,3,10,1]
=> by binary search, we cannot get to the smallest target interval
"""


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
