def dp(T, M, time, value):
    backpack = [0] * (T + 1)
    for i in range(M):
        for j in range(T, time[i] - 1, -1):
            backpack[j] = max(value[i] + backpack[j - time[i]], backpack[j])
    return backpack[T]


T, M = map(int, input().split())
time, value = [], []
for _ in range(M):
    t, v = map(int, input().split())
    time.append(t)
    value.append(v)
print(dp(T, M, time, value))
