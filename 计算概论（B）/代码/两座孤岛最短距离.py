def dfs(x, y):
    coordinate = []
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        island[i][j] = "0"
        coordinate.append((x, y))
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if island[nx][ny] == "1":
                    stack.append((nx, ny))
                    island[nx][ny] = "0"
    return coordinate


direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
n = int(input())
island = []
for _ in range(n):
    island.append(list(input()))
m = len(island[0])
flag = True
for i in range(n):
    for j in range(m):
        if island[i][j] == "1" and flag:
            lst_1 = dfs(i, j)
            flag = False
flag = True
for i in range(n):
    for j in range(m):
        if island[i][j] == "1" and flag:
            lst_2 = dfs(i, j)
            flag = False
dist = float("inf")
for a, b in lst_1:
    for c, d in lst_2:
        dist = min(dist, abs(a - c) + abs(b - d))
print(dist - 1)
