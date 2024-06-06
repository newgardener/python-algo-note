from typing import List
from collections import defaultdict
import heapq

"""
Time Complexity: O(nlogk) where n=len(nums), k
"""


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


"""
Bucket Sort
Time Complexity: O(n)
[1, 1, 1, 2, 2, 3]
count(i): [0, 1, 2, 3, 4, 5, 6]
num: [0, [3], [2], [1], [], [], []]
"""


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = count[n].get(n, 0) + 1
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
