def dfs(x,y,m,n,path,visited):
    cnt=0
    visited[x][y]=True
    if len(path)==m*n:
        cnt+=1
    for dx,dy in direction:
        nx,ny=x+dx,y+dy
        if 0<=nx<=n-1 and 0<=ny<=m-1 and not visited[nx][ny]:
            path.append((nx,ny))
            cnt+=dfs(nx,ny,m,n,path,visited)
            path.pop()
    visited[x][y]=False
    return cnt

ans,direction=[],[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,-2),(-1,2)]
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    path,visited=[(x,y)],[[False for _ in range(m)] for _ in range(n)]
    cnt=dfs(x,y,m,n,path,visited)
    ans.append(cnt)
for answer in ans:
    print(answer)
   