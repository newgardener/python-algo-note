def largestSubmatrix(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])

    for r in range(1, m):
        for c in range(n):
            if matrix[r][c] == 1:
                matrix[r][c] += matrix[r - 1][c]

    maxArea = 0
    for r in range(m):
        # we can rearrange columns of matrix in descending order to find the maxArea
        matrix[r].sort(reverse=True)
        for c in range(n):
            width = c + 1
            height = matrix[r][c]
            maxArea = max(maxArea, width * height)
    return maxArea
