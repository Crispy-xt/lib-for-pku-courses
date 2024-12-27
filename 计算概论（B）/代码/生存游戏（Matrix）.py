n, m = map(int, input().split())
matrix = [[0 for _ in range(m + 2)]]
for _ in range(n):
    row = list(map(int, input().split()))
    row.append(0)
    row.insert(0, 0)
    matrix.append(row)
matrix.append([0 for _ in range(m + 2)])
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s = (
            matrix[i - 1][j - 1]
            + matrix[i - 1][j]
            + matrix[i - 1][j + 1]
            + matrix[i][j - 1]
            + matrix[i][j + 1]
            + matrix[i + 1][j - 1]
            + matrix[i + 1][j]
            + matrix[i + 1][j + 1]
        )
        if matrix[i][j] == 1:
            if s < 2 or s >= 4:
                print(0, end=" ")
            else:
                print(1, end=" ")
        else:
            if s == 3:
                print(1, end=" ")
            else:
                print(0, end=" ")
    print()
