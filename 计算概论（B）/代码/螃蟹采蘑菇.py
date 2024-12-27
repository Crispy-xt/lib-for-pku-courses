n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
path=[]
for i in range(n):
    for j in range(n):
        if matrix[i][j]==5:
            path.append((i,j))
        if matrix[i][j]==9:
            a,b=i,j

direction=[(1,0),(0,1),(-1,0),(0,-1)]
visited=[[False for _ in range(n)] for _ in range(n)]
ans="no"
while path:
    i,j=path.pop()
    k,l=path.pop()
    for dx,dy in direction:
        di,dj,dk,dl=i+dx,j+dy,k+dx,l+dy
        if 0<=di<=n-1 and 0<=dj<=n-1 and 0<=dk<=n-1 and 0<=dl<=n-1:
            if matrix[di][dj]!=1 and matrix[dk][dl]!=1:
                if not visited[di][dj] or not visited[dk][dl]:
                    path.append((dk,dl))
                    path.append((di,dj))
                    visited[di][dj]=True
                    visited[dk][dl]=True
    if visited[a][b]:
        ans="yes"
        break
print(ans)


