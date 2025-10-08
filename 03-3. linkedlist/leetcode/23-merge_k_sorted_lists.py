"""
Divide and Conquer

Time Complexity:
given K = number of linked lists, N = average number of nodes in each linked list
Round 1: k/2 merges of 2n nodes each → kn work
Round 2: k/4 merges of 4n nodes each → kn work
Round 3: k/8 merges of 8n nodes each → kn work
...
Total rounds: log k
Total: O(kn log k)
Space Complexity: O(1)
- only uses a few pointers, regardless of the input size.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next

#%%
"""
Min Heap

Time Complexity:
Total nodes to process: kn
Each node: 1 heap pop + 1 heap push → 2 log k operations
Total: O(kn × log k) = O(kn log k)
Space Complexity: O(k)
"""

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                # should pass index as a time breaker when two nodes have same value
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))

        return dummy.next