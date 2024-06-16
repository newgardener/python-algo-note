from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    maxArea = 0
    stack = []

    for i, height in enumerate(heights):
        start = i
        while stack and stack[-1][1] > height:
            pi, ph = stack.pop()
            maxArea = max(maxArea, (i - pi) * ph)
            start = pi
        stack.append((start, height))

    while stack:
        pi, ph = stack.pop()
        maxArea = max(maxArea, (n - pi) * ph)

    return maxArea
