matrix = [[0 for _ in range(1025)] for _ in range(1025)]
d = int(input())
n = int(input())
max_sweep = 0
cnt = 0
for _ in range(n):
    i, j, t = map(int, input().split())
    a1, a2, b1, b2 = (
        max(0, i - d),
        min(1024, i + d),
        max(0, j - d),
        min(1024, j + d),
    )
    for k in range(a1, a2 + 1):
        for l in range(b1, b2 + 1):
            matrix[k][l] += t
            if matrix[k][l] == max_sweep:
                cnt += 1
            elif matrix[k][l] > max_sweep:
                max_sweep, cnt = matrix[k][l], 1

print(cnt, max_sweep)
