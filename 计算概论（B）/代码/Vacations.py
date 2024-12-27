n = int(input())
lst = list(map(int, input().split()))
dp = [0] * (n)
is_rest = False
if lst[0] == 0:
    dp[0] = 1
    is_rest = True
for i in range(1, n):
    if lst[i] != 3:
        if lst[i] == 0 or (
            (lst[i] == lst[i - 1] == 1 or lst[i] == lst[i - 1] == 2) and not is_rest
        ):
            dp[i] = dp[i - 1] + 1
            is_rest = True
        else:
            dp[i] = dp[i - 1]
            is_rest = False
    elif 1 <= lst[i - 1] <= 2 and not is_rest:
        lst[i] = 3 - lst[i - 1]
        dp[i] = dp[i - 1]
    elif lst[i] == 0:
        dp[i] = dp[i - 1] + 1
        is_rest = True
    else:
        dp[i] = dp[i - 1]
        is_rest = False
print(dp[n - 1])
