n, capacity = map(int, input().split())
value = list(map(int, input().split()))
weight = list(map(int, input().split()))
dp = [0] * (capacity + 1)
for i in range(n):
    for j in range(capacity, weight[i] - 1, -1):
        dp[j] = max(dp[j], value[i] + dp[j - weight[i]])
print(dp[capacity])
