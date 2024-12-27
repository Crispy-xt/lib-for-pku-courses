def times(l, r, x, a, b):
    m = min(a, b)
    M = max(a, b)
    a, b = m, M
    if a == b:
        return 0
    if a < l or b > r:
        return -1
    if b - l < x and r - b < x:
        return -1
    if a - l < x and r - a < x:
        return -1
    if b - a >= x:
        return 1
    if a - l >= x:
        return 2
    if r - b >= x:
        return 2
    return 3


n = int(input())
ans = []
for _ in range(n):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    ans.append(times(l, r, x, a, b))
for answer in ans:
    print(answer)
