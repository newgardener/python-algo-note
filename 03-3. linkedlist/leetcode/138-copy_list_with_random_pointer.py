from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    oldToNew = {None: None}

    cur = head
    while cur:
        oldToNew[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur:
        copy = oldToNew[cur]
        copy.next = oldToNew[cur.next]
        copy.random = oldToNew[cur.random]
        cur = cur.next

    return oldToNew[head]
