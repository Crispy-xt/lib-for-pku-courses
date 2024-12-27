from functools import lru_cache
@lru_cache(maxsize=None)

def dfs(x,y):
    for dx,dy in direction:
        nx,ny=x+dx,y+dy
        if 0<=nx<=r-1 and 0<=ny<=c-1 and matrix[nx][ny]<matrix[x][y]:
            dp[x][y]=max(1+dfs(nx,ny),dp[x][y])
    return dp[x][y]

r,c=map(int,input().split())
matrix=[]
for _ in range(r):
    matrix.append(list(map(int,input().split())))

dp=[[0 for _ in range(c)] for _ in range(r)]
direction=[(0,1),(1,0),(-1,0),(0,-1)]

m=0
for i in range(r):
    for j in range(c):
        m=max(m,dfs(i,j))
print(m+1)


