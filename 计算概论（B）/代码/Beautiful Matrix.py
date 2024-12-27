def steps(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                a, b = i + 1, j + 1
                break
    return abs(a - 3) + abs(b - 3)


matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
print(steps(matrix))
