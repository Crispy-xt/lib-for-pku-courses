n,m=map(int,input().split())
lst=list(map(int,input().split()))
dp=[10000000]*(m+1)
for ele in lst:
    if ele<=m:
        dp[ele]=1
for i in range(1,m+1):
    for coin in lst:
        if i>coin:
            dp[i]=min(dp[i],dp[i-coin]+1)
print(dp[m] if dp[m]!=10000000 else -1)