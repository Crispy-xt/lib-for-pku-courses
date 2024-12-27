import heapq
def dijkstra(x1,y1,x2,y2,matrix):
    if matrix[x1][y1]=="#" or matrix[x2][y2]=="#":
        return "NO"
    queue=[(0,x1,y1)]
    visited=[[False for _ in range(n)] for _ in range(m)]
    visited[x1][y1]=True
    matrix[x1][y1]=int(matrix[x1][y1])
    while queue:
        dist,x,y=heapq.heappop(queue)
        if x==x2 and y==y2:
            return dist
        visited[x][y]=True
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<=m-1 and 0<=ny<=n-1 and not visited[nx][ny]:
                if matrix[nx][ny]!="#":
                    matrix[nx][ny]=int(matrix[nx][ny])
                    heapq.heappush(queue,(dist+abs(matrix[nx][ny]-matrix[x][y]),nx,ny))
    return "NO"

ans=[]
directions=[(-1,0),(0,-1),(1,0),(0,1)]
m,n,p=map(int,input().split())
matrix=[]
for _ in range(m):
    matrix.append(list(input().split()))
for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    ans.append(dijkstra(x1,y1,x2,y2,matrix))
for answer in ans:
    print(answer)

