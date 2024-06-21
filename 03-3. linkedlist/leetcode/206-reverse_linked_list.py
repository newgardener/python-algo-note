from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    reversed = None
    current = head
    while current:
        node = current
        current = current.next
        node.next = reversed
        reversed = node
    return reversed
