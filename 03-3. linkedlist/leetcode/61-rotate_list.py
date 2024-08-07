from typing import Optional

"""
LinedList Rotation
Time Complexity: O(N)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        last = head
        length = 1
        while last and last.next:
            last = last.next
            length += 1

        k = k % length
        if k == 0:
            return head

        newTail = head
        for _ in range(length - k - 1):
            newTail = newTail.next

        # rotate list
        newHead = newTail.next
        last.next = head
        newTail.next = None
        return newHead
