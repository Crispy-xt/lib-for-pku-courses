n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
