n, a, b, c = map(int, input().split())
dp = [0] * (n + 1)
for i in range(min(a, b, c), n + 1):
    if (i >= a and dp[i - a] > 0) or i == a:
        dp[i] = dp[i - a] + 1
    if (i >= b and dp[i - b] > 0) or i == b:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if (i >= c and dp[i - c] > 0) or i == c:
        dp[i] = max(dp[i], dp[i - c] + 1)
print(dp[n])
