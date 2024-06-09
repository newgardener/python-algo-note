from typing import List

"""
Time Complexity: O(N)
"""


def trap(height: List[int]) -> int:
    leftMax, rightMax = 0, height[-1]
    l, r = 0, len(height) - 1
    trap = 0

    while l < r:
        leftMax = max(leftMax, height[l])
        rightMax = max(rightMax, height[r])
        if height[l] < leftMax:
            trap += leftMax - height[l]
        if height[r] < rightMax:
            trap += rightMax - height[r]

        if leftMax <= rightMax:
            l += 1
        else:
            r -= 1

    return trap
