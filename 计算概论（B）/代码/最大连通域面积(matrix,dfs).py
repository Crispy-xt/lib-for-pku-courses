def dfs(x,y):
    direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    stack=[(x,y)]
    field[x][y]="."
    s=1
    while stack:
        x,y=stack.pop()
        for dx,dy in direction:
            if 0<=x+dx<=m-1 and 0<=y+dy<=n-1 and field[x+dx][y+dy]=="W":
                stack.append((x+dx,y+dy))
                field[x+dx][y+dy]="."
                s+=1
    return s

ans=[]
for _ in range(int(input())):
    m,n=map(int,input().split())
    field=[]
    max_area=0
    for i in range(m):
        field.append(list(input()))
    for i in range(m):
        for j in range(n):
            if field[i][j]=="W":
                max_area=max(dfs(i,j),max_area)
    ans.append(max_area)
for answer in ans:
    print(answer)

    