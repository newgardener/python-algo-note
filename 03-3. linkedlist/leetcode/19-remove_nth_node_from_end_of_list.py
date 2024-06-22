from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return None

    # find kth node from the end
    # first - move fast pointer by n
    slow = fast = head
    while n > 0 and fast:
        fast = fast.next
        n -= 1

    # second - move slow and fast pointer together until fast pointer is valid
    prev = slow
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next

    if slow == head:
        head = head.next
    else:
        prev.next = slow.next

    return head
