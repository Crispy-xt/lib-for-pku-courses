m,n,k=map(int,input().split())
mat=[[0 for _ in range(n)] for _ in range(m)]
cnt=0
for _ in range(k):
    r,s,p,t=map(int,input().split())
    p=(p-1)//2
    i_1,i_2,j_1,j_2=max(1,r-p),min(r+p,m),max(1,s-p),min(s+p,n)
    for i in range(i_1-1,i_2):
            for j in range(j_1-1,j_2):
                if t:
                    mat[i][j]+=1
                else:
                    mat[i][j]-=1    
    if t:
        cnt+=1
possible_position=0
for i in range(m):
     for j in range(n):
          if mat[i][j]==cnt:
               possible_position+=1
print(possible_position)