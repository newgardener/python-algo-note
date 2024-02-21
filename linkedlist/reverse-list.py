class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next  # store next node
            current.next = prev  # reverse the link
            prev = current  # move one step forward in the list
            current = next_node  # move one step forward in the list
        return prev  # prev is now pointing to the new head
