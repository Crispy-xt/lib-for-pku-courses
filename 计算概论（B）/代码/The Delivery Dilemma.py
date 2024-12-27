t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    lst = []
    min_time = 0
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    for i in range(n):
        lst.append((lst_a[i], lst_b[i]))
        min_time += lst_b[i]
    lst.sort()
    pre_sum = []
    t = 0
    for i in range(n):
        t += lst[i][1]
        pre_sum.append(t)
    for i in range(n):
        s = lst[i][0]
        min_time = min(max(s, pre_sum[n - 1] - pre_sum[i]), min_time)
    ans.append(min_time)
for answer in ans:
    print(answer)
