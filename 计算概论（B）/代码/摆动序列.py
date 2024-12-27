n = int(input())
lst = list(map(int, input().split()))
dp_up = [1] * n
dp_down = [1] * n
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if lst[j] > lst[i]:
            dp_up[i] = max(dp_up[i], dp_down[j] + 1)
        if lst[j] < lst[i]:
            dp_down[i] = max(dp_down[i], dp_up[j] + 1)
print(max(max(dp_down, dp_up)))
