r = int(input())
ans = []
for _ in range(r):
    n, m, b = map(int, input().split())
    time, power, time_lst = [], [], []
    dict = {}
    for _ in range(n):
        t, x = map(int, input().split())
        time.append(t)
        power.append(x)
        if t not in time_lst:
            time_lst.append(t)
    for t in time_lst:
        dict[t] = []
    for i in range(n):
        dict[time[i]].append(power[i])
    for t in time_lst:
        if len(dict[t]) <= m:
            dict[t] = sum(dict[t])
        else:
            dict[t].sort(reverse=True)
            dict[t] = sum(dict[t][:m])
    time_lst.sort()
    for t in time_lst:
        current_time = t
        b -= dict[t]
        if b <= 0:
            ans.append(current_time)
            break
    if b > 0:
        ans.append("alive")
for answer in ans:
    print(answer)
