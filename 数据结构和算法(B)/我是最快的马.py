from collections import deque

board = [[0 for _ in range(11)] for _ in range(11)]
visited = [[False for _ in range(11)] for _ in range(11)]
a, b = map(int, input().split())
target_x, target_y = map(int, input().split())
direction = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
d = {1: 0, -1: 0, 2: 1, -2: -1}
q = deque([([a], [b], 0)])
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
ans = []
answer = float("inf")
visited[a][b] = True
while q:
    path_x, path_y, step = q.popleft()
    x, y = path_x[-1], path_y[-1]
    if x == target_x and y == target_y:
        ans.append((path_x, path_y))
        answer = step
    if step > answer:
        break
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if (
            0 <= nx <= 10
            and 0 <= ny <= 10
            and not board[nx][ny]
            and not board[x + d[dx]][y + d[dy]]
        ):
            new_path_x = path_x + [nx]
            new_path_y = path_y + [ny]
            q.append((new_path_x, new_path_y, step + 1))
if len(ans) > 1:
    print(len(ans))
else:
    path_x, path_y = ans[0]
    print("-".join([f"({path_x[i]},{path_y[i]})" for i in range(answer + 1)]))
