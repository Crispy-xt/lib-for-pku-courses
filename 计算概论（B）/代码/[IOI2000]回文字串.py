def min_insert(str):
    n = len(str)
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n + 1 - l):
            j = i + l - 1
            if str[i] == str[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


str = input()
print(min_insert(str))
"""递归方法 超时
def min_insert(str):
    n = len(str)
    if n == 0 or n == 1:
        return 0
    if n == 2:
        if str[0] == str[1]:
            return 0
        else:
            return 1
    else:
        if str[0] == str[-1]:
            return min_insert(str[1 : n - 1])
        else:
            return min(min_insert(str[1:]), min_insert(str[: n - 1])) + 1


str = input()
print(min_insert(str))"""
