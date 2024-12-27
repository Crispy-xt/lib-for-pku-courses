n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][1] = 1
for i in range(n + 1):
    for j in range(n + 1):
        if i > j:
            dp[i][j] = dp[i - j][j] + dp[i - 1][j - 1]
        if i == j:
            dp[i][j] = 1
print(dp[n][k])
