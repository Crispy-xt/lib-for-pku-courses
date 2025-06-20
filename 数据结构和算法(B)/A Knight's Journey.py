def dfs(x, y, p, q, path, visited):
    if p==q==1:
        return 'A1'
    if len(path) == p * q:
        return "".join(f"{alphabet[y]}{x+1}" for x, y in path)
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= p - 1 and 0 <= ny <= q - 1 and not visited[nx][ny]:
            path.append((nx, ny))
            visited[nx][ny] = True
            result = dfs(nx, ny, p, q, path, visited)
            if result != "impossible":
                return result
            nx, ny = path.pop()
            visited[nx][ny] = False
    return "impossible"


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = []
direction = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1),(-1, 2),(1, 2)]
for _ in range(int(input())):
    results = []
    p, q = map(int, input().split())
    visited = [[False for _ in range(q)] for _ in range(p)]
    path = [(0, 0)]
    visited[0][0] = True
    answer.append(dfs(0, 0, p, q, path, visited))
for i, ans in enumerate(answer):
    print(f"Scenario #{i+1}:")
    print(ans)
    print()
