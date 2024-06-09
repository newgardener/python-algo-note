from typing import List

"""
Time Complexity: O(N)
"""


def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    trap = 0

    while l < r:
        if leftMax <= rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            trap += leftMax - height[l]
        else:
            r += 1
            rightMax = max(rightMax, height[r])
            trap += rightMax - height[r]
    return trap
