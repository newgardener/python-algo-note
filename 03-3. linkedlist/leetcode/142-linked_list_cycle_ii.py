from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# find a point where cycle starts
def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return slow
    return None
