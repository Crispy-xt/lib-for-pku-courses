n=int(input())
dp = [[0 for _ in range(n+1)] for _ in range(n + 1)]  # dp[i][j]表示和为i，每个数小于等于j的分解个数
for i in range(1, n + 1):
    dp[i][1] = 1
    for j in range(2, n+1):
        if j <= i:
            s = 0
            for t in range(1, j + 1):
                s += dp[i - t][j]
            if j == i:
                dp[i][j] = (s + 1)
            else:
                dp[i][j] = s 
        else:
            dp[i][j] = dp[i][j - 1]
print((dp[n][n]))
