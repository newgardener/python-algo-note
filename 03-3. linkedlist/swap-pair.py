class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def swapPairs(self, head: Node) -> Node:
        # prevNode를 관리하기 위한 방법으로 dummyNode 생성
        dummyNode = Node(-1)
        dummyNode.next = head
        prevNode = dummyNode

        while head and head.next:
            firstNode = head
            secondNode = head.next

            firstNode.next = secondNode.next
            secondNode.next = firstNode
            prevNode.next = secondNode

            prevNode = firstNode
            head = firstNode.next

        return dummyNode.next
