from collections import deque
def bfs(field):
    direction=[(-1,0),(1,0),(0,1),(0,-1)]
    dist=[[float("inf") for _ in range(m)] for _ in range(n)]
    x,y=0,0
    dist[0][0]=0
    lst=deque([(x,y)])
    while lst:
        x,y=lst.popleft()
        for dx,dy in direction:
            if 0<=x+dx<=n-1 and 0<=y+dy<=m-1 and field[x+dx][y+dy]!=2 and dist[x+dx][y+dy]==float("inf"):
                dist[x+dx][y+dy]=min(dist[x+dx][y+dy],1+dist[x][y])
                lst.append((x+dx,y+dy))
    return dist
n,m=map(int,input().split())
field=[]
for i in range(n):
    field.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if field[i][j]==1:
            x,y=i,j
            break
dist=bfs(field)
if dist[x][y]==float("inf"):
    print("NO")
else:
    print(dist[x][y])
