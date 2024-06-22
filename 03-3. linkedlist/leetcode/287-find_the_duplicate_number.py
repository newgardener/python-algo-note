from typing import List


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
