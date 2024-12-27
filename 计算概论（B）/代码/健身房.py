T, n = map(int, input().split())
dp = [-float("inf")] * (T + 1)
dp[0] = 0
time, mass = [], []
for _ in range(n):
    t, m = map(int, input().split())
    time.append(t)
    mass.append(m)

for i in range(n):
    for j in range(T, time[i] - 1, -1):
        if dp[j - time[i]] != -float("inf"):
            dp[j] = max(dp[j], dp[j - time[i]] + mass[i])
print(dp[T] if dp[T] != -float("inf") else -1)
