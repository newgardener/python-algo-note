import heapq

"""_summary_
 smaller than x <= median x <= larger than x
 - smallNumList is handled by maxHeap getting largest among smallNumList
 - bigNumList is handled by minHeap getting smallest among bigNumList
 - maxHeap should always contain one more number compared to minHeap
"""


class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insertNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        # if even number,
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        # if odd number,
        return self.maxHeap[0] / 1.0
