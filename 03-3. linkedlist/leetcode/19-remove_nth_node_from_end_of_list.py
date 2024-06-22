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

    # case where target node is the head
    if slow == head:
        head = head.next
    else:
        prev.next = slow.next

    return head


def neetCodeSolution(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # create dummy node to point prior to the target node
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next
    return dummy.next
