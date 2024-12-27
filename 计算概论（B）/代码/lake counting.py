# using stack --> dfs:
def dfs(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for dx, dy in direction:
            if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1:
                if matrix[x + dx][y + dy] == "W":
                    stack.append((x + dx, y + dy))
                    matrix[x + dx][y + dy] = "."


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
cnt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "W":
            matrix[i][j] = "."
            dfs(i, j)
            cnt += 1
print(cnt)


# recursion and dfs:
"""import sys

sys.setrecursionlimit(30000)


def dfs(x, y):
    matrix[x][y] = "."
    for dx, dy in direction:
        if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1:
            if matrix[x + dx][y + dy] == "W":
                dfs(x + dx, y + dy)


n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
cnt = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "W":
            dfs(i, j)
            cnt += 1
print(cnt)"""
