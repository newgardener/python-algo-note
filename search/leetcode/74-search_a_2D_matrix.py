# https://leetcode.com/problems/search-a-2d-matrix
# https://leetcode.com/problems/search-a-2d-matrix-ii
"""
Time Complexity: O(m+n) if m = # of row, n = # of column
"""

from typing import List


def searchMatrixI(matrix: List[List[int]], target: int) -> bool:
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


def searchMatrixII(matrix: List[List[int]], target: int) -> bool:
    def binarySearch(left, right, arr):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right if right >= 0 else -1

    colLeft, colRight = 0, len(matrix[0]) - 1
    colIndex = binarySearch(colLeft, colRight, matrix[0])

    while colIndex >= 0:
        rowLeft, rowRight = 0, len(matrix) - 1
        rowIndex = binarySearch(rowLeft, rowRight, [item[colIndex] for item in matrix])
        if matrix[rowIndex][colIndex] == target:
            return True
        colIndex -= 1
    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 5
print(searchMatrixII(matrix, target))
