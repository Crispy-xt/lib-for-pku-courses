n=int(input())
matrix=[]
ans=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
if n==1:
    print(matrix[0][0])
elif n==2:
    print(sum(matrix[0])+sum(matrix[1]))
else:
    for i in range(n//2):
        s=0
        for j in range(i,n-i):
            s+=(matrix[i][j]+matrix[n-i-1][j])
        for j in range(i+1,n-1-i):
            s+=(matrix[j][i]+matrix[j][n-i-1])
        ans.append(s)
    i=n//2
    if n%2:
        ans.append(matrix[i][i])
    print(max(ans))
        
