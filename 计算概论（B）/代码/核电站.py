n,m=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
if n<m:
    print(2**n)
else:
    for i in range(1,m):
        dp[i]=2**i
    for i in range(m,n+1):
        for j in range(1,m+1):
            dp[i]+=dp[i-j]
    print(dp[n])