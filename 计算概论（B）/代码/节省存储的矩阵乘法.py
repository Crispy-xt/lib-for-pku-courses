n,m1,m2=map(int,input().split())
x,y,z=[[0 for _ in range(n)] for _ in range(n)],[[0 for _ in range(n)] for _ in range(n)],[[0 for _ in range(n)] for _ in range(n)]
for _ in range(m1):
    a,b,c=map(int,input().split())
    x[a][b]=c
for _ in range(m2):
    a,b,c=map(int,input().split())
    y[a][b]=c
for i in range(n):
    for j in range(n):
        for k in range(n):
            z[i][j]+=x[i][k]*y[k][j]
ans=[]
for i in range(n):
    for j in range(n):
        if z[i][j]!=0:
            ans.append([i,j,z[i][j]])
for ele in ans:
    print(ele[0],ele[1],ele[2])


