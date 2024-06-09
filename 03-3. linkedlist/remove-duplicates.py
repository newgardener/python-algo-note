class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def printList(self, head):
        current = head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    solution = Solution()

    # Test Example 1
    head1 = Node(1, Node(1, Node(2)))
    result1 = solution.deleteDuplicates(head1)  # Expected: 1 -> 2
    solution.printList(result1)

    # Test Example 2
    head2 = Node(1, Node(2, Node(2, Node(3))))
    result2 = solution.deleteDuplicates(head2)  # Expected: 1 -> 2 -> 3
    solution.printList(result2)
