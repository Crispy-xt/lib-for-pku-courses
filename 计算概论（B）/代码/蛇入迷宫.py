from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
visited = [[[False for _ in range(2)] for _ in range(n)] for _ in range(n)]
direction = [(1, 0), (0, 1)]
flag = 0
q = deque([(0, 0, 0, flag)])
visited[0][0][0] = True
while q:
    dist, x, y, flag = q.popleft()
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if flag:
            if (
                0 <= nx <= n - 2
                and 0 <= ny <= n - 1
                and matrix[nx][ny] == matrix[nx + 1][ny] == 0
                and not visited[nx][ny][flag]
            ):
                q.append((dist + 1, nx, ny, flag))
                visited[nx][ny][flag] = True
        else:
            if (
                0 <= nx <= n - 1
                and 0 <= ny <= n - 2
                and matrix[nx][ny] == matrix[nx][ny + 1] == 0
                and not visited[nx][ny][flag]
            ):
                if nx == n - 1 and ny == n - 2:
                    print(dist + 1)
                    exit()
                q.append((dist + 1, nx, ny, flag))
                visited[nx][ny][flag] = True
    if flag:
        if (
            y != n - 1
            and matrix[x][y + 1] == matrix[x + 1][y + 1] == 0
            and not visited[x][y][1 - flag]
        ):
            q.append((dist + 1, x, y, 1 - flag))
            visited[x][y][1 - flag] = True
    else:
        if (
            x != n - 1
            and matrix[x + 1][y] == matrix[x + 1][y + 1] == 0
            and not visited[x][y][1 - flag]
        ):
            q.append((dist + 1, x, y, 1 - flag))
            visited[x][y][1 - flag] = True
print(-1)
