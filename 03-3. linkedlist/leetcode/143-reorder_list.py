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
    secondHead = slow.next
    slow.next = None

    first = head
    second = secondHead

    # reverse the second part
    reversed = None
    current = second
    while current:
        node = current
        current = current.next
        node.next = reversed
        reversed = node

    result = ListNode()
    current = result
    while first and reversed:
        firstNode = first
        reversedNode = reversed
        first = first.next
        reversed = reversed.next

        current.next = firstNode
        current.next.next = reversedNode
        current = current.next.next

    if first:
        current.next = first

    if reversed:
        current.next = reversed

    node = result.next
