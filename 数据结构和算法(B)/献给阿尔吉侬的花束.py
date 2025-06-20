from collections import deque
direction=[(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(int(input())):
    r,c=map(int,input().split())
    matrix=[]
    for _ in range(r):
        matrix.append(input())
    for i in range(r):
        for j in range(c):
            if matrix[i][j]=='S':
                start=(i,j)
                break
    see=set()
    i,j=start
    q=deque([(i,j,0)])
    find=False
    while q:
        if find:
            break
        x,y,step=q.popleft()
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if 0<=nx<=r-1 and 0<=ny<=c-1 and (nx,ny) not in see and matrix[nx][ny]!='#':
                if matrix[nx][ny]=='E':
                    find=True
                    print(step+1)
                    break
                q.append((nx,ny,step+1))
                see.add((nx,ny))
    if not find:
        print('oop!')
