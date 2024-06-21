from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
    l, r = list1, list2
    dummy = ListNode()

    current = dummy
    while l and r:
        if l.val <= r.val:
            current.next = l
            l = l.next
        else:
            current.next = r
            r = r.next
        current = current.next

    if l:
        current.next = l

    if r:
        current.next = r

    return dummy.next
