from collections import deque

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(board, x1, y1, x2, y2):
    m, n = len(board[0]), len(board)
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((x1, y1, 0, x1 ,y1))
    while queue:
        x, y, dist,u,v = queue.popleft()
        visited[y][x] = True
        if x == x2 and y == y2:
            return f"{dist} segments."
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
                if (board[ny][nx] != "X" and not visited[ny][nx]) or (nx == x2 and ny == y2):
                    if dx*(u-x)==dy*(v-y)==0:
                        pair=(nx, ny, dist + 1, x, y)
                    else:
                        pair=(nx, ny, dist, x, y)
                    queue.append(pair)
                    visited[ny][nx] = True
    return "impossible."


ans = []
while True:
    path = []
    w, h = map(int, input().split())
    if w * h == 0:
        break
    else:
        board = [[" "] * (w + 2)]
        for _ in range(h):
            row = [" "] + list(input()) + [" "]
            board.append(row)
        board.append([" "] * (w + 2))
        while True:
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == y1 == x2 == y2 == 0:
                break
            else:
                path.append(bfs(board, x1, y1, x2, y2))
    ans.append(path)
for i in range(len(ans)):
    print(f"Board #{i+1}:")
    for j in range(len(ans[i])):
        print(f"Pair {j+1}: {ans[i][j]}")
    print()
