from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]):
    """
    Do not return anything, modify head in-place instead.
    """
    # find a mid
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # disconnect first and second to avoid cycle
    second = slow.next
    slow.next = None

    prev = None
    while second:
        node = second.next
        second.next = prev
        prev = second
        second = node

    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
