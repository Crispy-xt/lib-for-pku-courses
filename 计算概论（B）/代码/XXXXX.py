t = int(input())
ans = []
for _ in range(t):
    pre_sum = [0]
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))
    sum = 0
    for i in range(1, n + 1):
        sum += lst[i - 1]
        sum = sum % x
        pre_sum.append(sum)
    dp = [-1] * (n + 1)
    max_gap = -1
    if pre_sum[0] != pre_sum[-1]:
        max_gap = n
    else:
        x, y = 1, n - 1
        while pre_sum[x] == pre_sum[x - 1] and x <= n - 1:
            x += 1
        while pre_sum[y] == pre_sum[y + 1] and y >= 1:
            y -= 1
        if x != n or y != 0:
            max_gap = max(n - x, y)
    ans.append(max_gap)
for answer in ans:
    print(answer)
