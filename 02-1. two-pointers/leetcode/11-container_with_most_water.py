from typing import List


def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    area = 0
    while l < r:
        # update maxArea narrowing down the search space
        area = max(area, min(height[l], height[r]) * (r - l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return area
