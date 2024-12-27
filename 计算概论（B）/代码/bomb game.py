m, n, k = map(int, input().split())
matrix = [[1 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    r, s, p, t = map(int, input().split())
    r -= 1
    s -= 1
    if t == 1:
        for i in range(m):
            for j in range(n):
                if abs(i - r) > p / 2 or abs(j - s) > p / 2:
                    matrix[i][j] = 0
    else:
        for i in range(m):
            for j in range(n):
                if abs(i - r) <= p / 2 and abs(j - s) <= p / 2:
                    matrix[i][j] = 0
s = 0
for i in range(m):
    s += sum(matrix[i])
print(s)
