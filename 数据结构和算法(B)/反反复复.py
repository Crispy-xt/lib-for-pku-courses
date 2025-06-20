n = int(input())
s = input()
l = len(s)
m = l // n
matrix = []
for i in range(m):
    if i % 2 == 0:
        matrix.append(list(s[n * i : n * i + n]))
    else:
        matrix.append(list(s[n * i + n - 1 : n * i - 1 : -1]))
for i in range(n):
    for j in range(m):
        print(matrix[j][i], end="")
