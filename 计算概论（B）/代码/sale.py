n, m = map(int, input().split())
lst = sorted(map(int, input().split()))
sum = 0
for i in range(m):
    if lst[i] >= 0:
        break
    sum += lst[i]
print(-sum)
