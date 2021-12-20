n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(map(int, input().split()))

result = 0
for i in range(n):
    result = max(result, min(matrix[i]))

print(result)
