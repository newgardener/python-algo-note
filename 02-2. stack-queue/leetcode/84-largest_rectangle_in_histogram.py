"""
Stack
Space Complexity: O(N)
Time Complexity: O(N) 
"""


def largestRectangleArea(heights: list[int]) -> int:
    n = len(heights)
    leftmost = [-1] * n # left outer bound

    stack = []
    # find first smaller element to the left
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftmost[i] = stack[-1]
        stack.append(i)

    rightmost = [n] * n # right outer bound
    stack = []
    # find first smaller element to the right
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rightmost[i] = stack[-1]
        stack.append(i)

    maxArea = 0
    for i in range(n):
        h = heights[i]
        maxArea = max(maxArea, (rightmost[i] - leftmost[i] - 1) * h, h)
    return maxArea


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
