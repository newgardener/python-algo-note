"""
1. Popping Elements: O(n * log k)
2. Final Pop: O(1)
=> Time Complexity: O(nlogk)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            heapq.heappush(arr, num)
            if len(arr) > k:
                heapq.heappop(arr)
        return arr[0]
