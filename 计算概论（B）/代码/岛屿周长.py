def calculate_island_perimeter(n, m, matrix):
    perimeter = 0
    for col in matrix:
        col.extend([0, 0])
        col.insert(0, 0)
        col.insert(0, 0)
    matrix.extend([[0 for _ in range(m + 4)] for _ in range(2)])
    matrix.insert(0, [0 for _ in range(m + 4)])
    matrix.insert(0, [0 for _ in range(m + 4)])
    for i in range(1, n + 3):
        for j in range(1, m + 3):
            if matrix[i][j] == 0:
                perimeter += (
                    matrix[i][j - 1]
                    + matrix[i][j + 1]
                    + matrix[i - 1][j]
                    + matrix[i + 1][j]
                )
    return perimeter


n, m = map(int, input().split())
matrix = []
for i in range(n):
    col = list(map(int, input().split()))
    matrix.append(col)
print(calculate_island_perimeter(n, m, matrix))
