def dfs(x, y, n, path, visited):
    if len(path) == n**2:
        return "success"
    candidates=[]
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and not visited[nx][ny]:
            degree=0
            for ddx,ddy in direction:
                nnx,nny=nx+ddx,ny+ddy
                if 0<=nnx<=n-1 and 0<=nny<=n-1 and not visited[nnx][nny]:
                    degree+=1
            candidates.append((degree,nx,ny))
    candidates.sort()
    for degree,nx,ny in candidates:
        path.append((nx, ny))
        visited[nx][ny] = True
        result = dfs(nx, ny, n, path, visited)
        if result != "fail":
            return result
        nx, ny = path.pop()
        visited[nx][ny] = False
    return "fail"

n=int(input())
x,y=map(int,input().split())
direction = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]
visited = [[False for _ in range(n)] for _ in range(n)]
path = [(x, y)]
visited[x][y] = True
answer=dfs(x, y, n, path, visited)
print(answer)
