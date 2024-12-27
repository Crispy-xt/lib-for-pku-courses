def dp(n, capacity, value, weight):
    if n == 0 or capacity == 0:
        return 0
    if weight[n - 1] > capacity:
        return dp(n - 1, capacity, value, weight)
    else:
        value_1 = value[n - 1] + dp(n - 1, capacity - weight[n - 1], value, weight)
        value_2 = dp(n - 1, capacity, value, weight)
        return max(value_1, value_2)


n, capacity = map(int, input().split())
value = []
weight = []
for _ in range(n):
    a, b = map(int, input().split())
    value.append(a)
    weight.append(b)
print(float(dp(n, capacity, value, weight)))
