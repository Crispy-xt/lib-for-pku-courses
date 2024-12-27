import sys
direction=[(1,0),(0,1),(-1,0),(0,-1)]
def dfs(matrix,x,y,a,b):
    m,n=len(matrix),len(matrix[0])
    h=matrix[x][y]
    stack=[(x,y)]
    flood=[[False for _ in range(n)] for _ in range(m)]
    while stack:
        x,y=stack.pop()
        flood[x][y]=True
        for dx,dy in direction:
            nx,ny=dx+x,dy+y
            if 0<=nx<=m-1 and 0<=ny<=n-1:
                if  not flood[nx][ny] and matrix[nx][ny]<matrix[x][y]:
                    flood[nx][ny]=True
                    matrix[nx][ny]=h
                    stack.append((nx,ny))
        if flood[a][b]:
            return True
    return flood[a][b]

ans=[]
data=sys.stdin.read
data=data().split()
k=int(data[0])
id=1
for _ in range(k):
    m,n=int(data[id]),int(data[id+1])
    id+=2
    matrix=[]
    for _ in range(m):
        matrix.append(list(map(int,data[id:id+n])))
        id+=n
    a,b=int(data[id])-1,int(data[id+1])-1
    id+=2
    pos=[]
    p=int(data[id])
    id+=1
    for _ in range(p):
        x,y=int(data[id])-1,int(data[id+1])-1
        pos.append((x,y))
        id+=2
    ans.append("Yes" if any(dfs(matrix,x,y,a,b) for x,y in pos) else "No")
sys.stdout.write("\n".join(ans)+"\n")