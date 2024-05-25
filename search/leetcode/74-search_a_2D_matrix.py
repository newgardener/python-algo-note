# https://leetcode.com/problems/search-a-2d-matrix
"""
Time Complexity: O(m+n) if m = # of row, n = # of column
"""

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    # initialize
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False
