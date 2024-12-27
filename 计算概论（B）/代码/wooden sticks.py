ans = []
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    a, b = [0] * n, [0] * n
    dp = [1] * n
    for i in range(n):
        a[i] = (lst[2 * i], lst[2 * i + 1])
    a.sort()
    for i in range(n):
        b[i] = a[i][1]
    for i in range(1, n):
        for j in range(i):
            if b[j] > b[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    ans.append(max(dp))
for answer in ans:
    print(answer)
