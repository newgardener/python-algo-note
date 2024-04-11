# %%
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# %%
def rotate_by_90(matrix):
    N = len(matrix)

    # transpose the matrix
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for i in range(N):
        matrix[i].reverse()

    return matrix


# %%
"""
matrix:
1 2 3
4 5 6
7 8 9
reverse each row:
3 2 1
6 5 4
9 8 7
reverse the order of row:
9 8 7
6 5 4
3 2 1
"""


def rotate_by_180(matrix):

    N = len(matrix)

    # reverse each row
    for i in range(N):
        matrix[i].reverse()
    # reverse the order of row
    matrix.reverse()

    return matrix


# %%
"""
matrix:
1 2 3
4 5 6
7 8 9
transpose:
1 4 7
2 5 8
3 6 9
reverse each column:
3 6 9
2 5 8
1 4 7
"""


def rotate_by_270(matrix):
    N = len(matrix)

    # transpose the matrix
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each column
    for i in range(N):
        for j in range(N // 2):
            matrix[j][i], matrix[N - j - 1][i] = matrix[N - j - 1][i], matrix[j][i]

    return matrix


# %%
import copy

print(rotate_by_90(copy.deepcopy(matrix)))
print(rotate_by_180(copy.deepcopy(matrix)))
print(rotate_by_270(copy.deepcopy(matrix)))

# %%
