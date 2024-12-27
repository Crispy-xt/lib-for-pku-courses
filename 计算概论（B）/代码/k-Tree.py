M=10**9+7
n, k, d = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # dp[i][j]表示和为i，每个数小于等于j的分解个数
for i in range(1,n + 1):
    dp[i][1] = 1
    for j in range(2, k+1):
        if j<=i:
            s = 0
            for t in range(1,j+1):
                s += dp[i-t][j]
            if j==i:
                dp[i][j]=(s+1)%M
            else:
                dp[i][j]=s%M
        else:
            dp[i][j]=dp[i][j-1]
print((dp[n][k] - dp[n][d - 1])%M)
