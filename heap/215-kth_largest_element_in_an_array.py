"""
1. Heapify: O(n)
2. Popping Elements: O((n-k) * log n)
3. Final Pop: O(log n)
=> Time Complexity: O(nlogn)
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
