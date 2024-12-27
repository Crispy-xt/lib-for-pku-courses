from collections import defaultdict

score=set()
d=defaultdict(int)
m,n=map(int,input().split())
pos=[0 for _ in range(m*n)]
for i in range(m):
    lst=list(map(int,input().split()))
    for j in range(n):
        pos[lst[j]]=(i,j)

matrix=[[0 for _ in range(n)] for _ in range(m)]
for k in range(m*n):
    lst=list(map(int,input().split()))
    s=sum(lst)
    score.add(s)
    d[s]+=1
    i,j=pos[k]
    matrix[i][j]=lst

cnt=0
direction=[(-1,0),(0,1),(0,-1),(1,0)]
for i in range(m):
    for j in range(n):
        for di,dj in direction:
            ni,nj=i+di,j+dj
            if 0<=ni<=m-1 and 0<=nj<=n-1:
                if matrix[ni][nj]==matrix[i][j]:
                    cnt+=1
                    break  

score=list(score)
score.sort(reverse=True)
limit=m*n*0.4
s=0
for ele in score:
    if s+d[ele]>limit:
        break
    s+=d[ele]

print(cnt,s)