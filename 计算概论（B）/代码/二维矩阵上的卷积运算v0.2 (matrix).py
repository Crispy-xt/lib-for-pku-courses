m, n, p, q = map(int, input().split())
A, B = [], []
for _ in range(m):
    row = list(map(int, input().split()))
    A.append(row)
for _ in range(p):
    row = list(map(int, input().split()))
    B.append(row)
x, y = m - p + 1, n - q + 1
C = [[0] * (n - q + 1) for _ in range(m - p + 1)]
for i in range(m - p + 1):
    for j in range(n - q + 1):
        s = 0
        for k in range(p):
            for l in range(q):
                s += A[i + k][j + l] * B[k][l]
        C[i][j] = s
for i in range(m - p + 1):
    for j in range(n - q + 1):
        print(C[i][j], end=" ")
    print("\r")
