from collections import deque
def locate(matrix,target):
    m,n=len(matrix),len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==target:
                return i,j

ans=[]
direction=[(0,1),(1,0),(-1,0),(0,-1)]
for _ in range(int(input())):
    r,c,k=map(int,input().split())
    matrix=[]
    for _ in range(r):
        matrix.append(list(input()))
    x,y=locate(matrix,"S")
    queue=deque()
    queue.append((x,y,0))
    visited=[[[False for _ in range(c)] for _ in range(r)] for _ in range(k)] 
    visited[0][x][y]=True
    flag=False
    while queue:
        x,y,t=queue.popleft()
        if matrix[x][y]=="E":
            ans.append(t)
            flag=True
            break
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if 0<=nx<=r-1 and 0<=ny<=c-1 and not visited[(t+1)%k][nx][ny]:
                if matrix[nx][ny]!="#" or (t+1)%k==0:
                    queue.append((nx,ny,t+1))
                    visited[(t+1)%k][nx][ny]=True
    if not flag:
        ans.append("Oop!")
for answer in ans:  
    print(answer)

    

