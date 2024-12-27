n, m = map(int, input().split())
lst = list(map(int, input().split()))
dp = [1] * (n + 1)
flag = [False] * (1 + max(lst))
flag[lst[-1]] = True
for i in range(n - 1, 0, -1):
    if flag[lst[i - 1]]:
        dp[i] = dp[i + 1]
    else:
        flag[lst[i - 1]] = True
        dp[i] = dp[i + 1] + 1
ans = []
for _ in range(m):
    l = int(input())
    ans.append(dp[l])
for answer in ans:
    print(answer)
