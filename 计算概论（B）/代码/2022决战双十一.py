n, m = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    lst = list(input().split())
    for ele in lst:
        a, b = ele.split(":")
        a, b = int(a), int(b)
        matrix[i].append((a, b))
discount = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    lst = list(input().split())
    for ele in lst:
        a, b = ele.split("-")
        a, b = int(a), int(b)
        discount[i].append((a, b))

backet = {i: 0 for i in range(1, m + 1)}
ans = float("inf")


def dfs(k):
    global ans
    if k == n + 1:
        s = sum([backet[i] for i in range(1, m + 1)])
        s -= (s // 300) * 50
        for i in range(1, m + 1):
            t = backet[i]
            max_discount = 0
            for a, b in discount[i]:
                if t >= a:
                    max_discount = max(max_discount, b)
            s -= max_discount
        ans = min(ans, s)
        return
    for i in range(len(matrix[k])):
        a, b = matrix[k][i]
        backet[a] += b
        dfs(k + 1)
        backet[a] -= b


dfs(1)
print(ans)
