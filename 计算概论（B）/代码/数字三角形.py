"""dp方法"""


def maxpath(triangle, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[n - 1] = triangle[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = triangle[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]


n = int(input())
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)
print(maxpath(triangle, n))


"""def max_path(triangle, n):
    if n == 1:
        return triangle[0][0]
    else:
        triangle_1 = []
        triangle_2 = []
        for i in range(1, n):
            row = list(triangle[i][:i])
            triangle_1.append(row)
        for i in range(1, n):
            row = list(triangle[i][1:])
            triangle_2.append(row)
        return (
            max(max_path(triangle_1, n - 1), max_path(triangle_2, n - 1))
            + triangle[0][0]
        )


n = int(input())
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)
print(max_path(triangle, n))
递归方法，超时"""
