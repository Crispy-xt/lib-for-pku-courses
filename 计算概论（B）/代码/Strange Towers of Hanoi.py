dp = [100000] * 13
dp[1] = 1
for i in range(2, 13):
    for j in range(1, i):
        dp[i] = min(dp[i], 2 * dp[j] + 2 ** (i - j) - 1)
for i in range(1, 13):
    print(dp[i])
