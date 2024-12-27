def max_increasing(lst):
    n = len(lst)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def max_decreasing(lst):
    n = len(lst)
    dp = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


max_remain = 0
n = int(input())
lst = list(map(int, input().split()))
increasing, decreasing = max_increasing(lst), max_decreasing(lst)
for i in range(n):
    max_remain = max(max_remain, increasing[i] + decreasing[i] - 1)
print(n - max_remain)
