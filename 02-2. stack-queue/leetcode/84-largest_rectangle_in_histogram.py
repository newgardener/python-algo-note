from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    maxArea = 0
    stack = []

    for i, height in enumerate(heights):
        if not stack or stack[-1][1] <= height:
            stack.append((i, height))
        else:
            lastIdx = -1
            while stack and stack[-1][1] > height:
                pi, ph = stack.pop()
                maxArea = max(maxArea, (i - pi) * ph)
                lastIdx = pi
            stack.append((lastIdx, height))

    while stack:
        pi, ph = stack.pop()
        maxArea = max(maxArea, (n - pi) * ph)

    return maxArea
