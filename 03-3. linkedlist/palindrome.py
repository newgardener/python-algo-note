class DLNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class Solution:
    def isPalindrome(self, head):
        # check base condition
        if not head or not head.next:
            return True

        tail = head
        while tail.next:
            tail = tail.next

        # set start and end DLNode
        start = head
        end = tail

        # if node count is odd -> start != end
        # if node count is even -> start.prev != end
        while start != end and start.prev != end:
            if start.val != end.val:
                return False

            start = start.next
            end = end.prev

        return True


if __name__ == "__main__":
    solution = Solution()

    head1 = DLNode(1)
    head1.next = DLNode(2)
    head1.next.prev = head1
    head1.next.next = DLNode(1)
    head1.next.next.prev = head1.next

    print(solution.isPalindrome(head1))
