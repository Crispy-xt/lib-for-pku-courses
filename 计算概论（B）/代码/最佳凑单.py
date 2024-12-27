n,t=map(int,input().split())
value=sorted(list(map(int,input().split())))
dp=[[0 for _ in range(t+1)]for _ in range(n+1)] #dp[i][j]表示用前i件商品对j元的最佳凑单
for i in range(1,n+1):
    j,s=1,sum(value[:i])
    while j<=min(s,t):
        if j>=value[i-1]:
            dp[i][j]=value[i-1]+dp[i-1][j-value[i-1]]
        else:
            dp[i][j]=value[i-1]
        if dp[i-1][j]:
            dp[i][j]=min(dp[i][j],dp[i-1][j])
        j+=1
print(dp[n][t])
        
