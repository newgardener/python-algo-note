from typing import List
from collections import defaultdict
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    numDict = defaultdict(int)
    for num in nums:
        numDict[num] += 1

    arr = []
    for key, value in numDict.items():
        if len(arr) < k:
            heapq.heappush(arr, (value, key))
        else:
            if arr[0][0] < value:
                heapq.heappop(arr)
                heapq.heappush(arr, (value, key))

    return [key for (value, key) in arr]
