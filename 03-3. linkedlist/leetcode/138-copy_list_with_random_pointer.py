from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    oldToCody = {None: None}

    cur = head
    while cur:
        oldToCody[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur:
        copy = oldToCody[cur]
        copy.next = oldToCody[cur.next]
        copy.random = oldToCody[cur.random]
        cur = cur.next

    return oldToCody[head]
