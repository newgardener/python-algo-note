from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    # base condition
    if not head or not head.next:
        return head

    # prev == mid position (subProblem 1)
    # slow == mid+1 position (subProblem 2)
    prev = None
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None
    l1 = sortList(head)
    l2 = sortList(slow)

    return merge(l1, l2)


def merge(l1, l2):
    dummy = tail = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next
