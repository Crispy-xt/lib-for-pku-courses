def dfs(x, y, current_value):
    global max_value, current_route, route
    if x == n - 1 and y == m - 1:
        if current_value > max_value:
            max_value = current_value
            route = current_route[:]
        return
    visited[x][y] = True
    for dx, dy in direction:
        if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1 and not visited[x + dx][y + dy]:
            current_value += matrix[x + dx][y + dy]
            current_route.append((x + dx + 1, y + dy + 1))
            dfs(x + dx, y + dy, current_value)
            a, b = current_route.pop()
            current_value -= matrix[a - 1][b - 1]
    visited[x][y] = False


n, m = map(int, input().split())
max_value = float("-inf")
current_route, route = [(1, 1)], []
visited = [[False for _ in range(m)] for _ in range(n)]
direction, matrix = [(0, 1), (1, 0), (0, -1), (-1, 0)], []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
dfs(0, 0, matrix[0][0])
for ele in route:
    x, y = ele
    print(x, y)
