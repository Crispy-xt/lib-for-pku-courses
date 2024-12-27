n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
x = lst[n - 1] - lst[0]
lst_minus = []
for i in range(n - 1):
    lst_minus.append(-lst[i + 1] + lst[i])
lst_minus.sort()
sum = 0
for i in range(m - 1):
    sum += lst_minus[i]
print(x + sum)
