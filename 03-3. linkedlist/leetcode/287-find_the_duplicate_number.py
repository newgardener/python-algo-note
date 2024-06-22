from typing import List


"""
Time Complexity: O(N)
1. figure out why this is linked list cycle problem
2. should apply Floyd's algorithm
"""


def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    # find an intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # find a starting cycle point
    slow = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            return slow
