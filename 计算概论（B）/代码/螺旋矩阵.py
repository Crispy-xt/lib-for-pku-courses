def is_block(x, y, matrix):
    if matrix[x][y] > 0:
        return True
    else:
        return False


n = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
turn_times = 0
matrix = [[1 for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        matrix[i][j] = 0
x, y = 1, 1
for k in range(1, n * n + 1):
    if not is_block(x + dx[turn_times], y + dy[turn_times], matrix):
        matrix[x][y] = k
        x += dx[turn_times]
        y += dy[turn_times]
    else:
        matrix[x][y] = k
        turn_times = (turn_times + 1) % 4
        x += dx[turn_times]
        y += dy[turn_times]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(matrix[j][i], end=" ")
    print()
