n = int(input())
lst = sorted(map(int, input().split()), reverse=True)
total = sum(lst)
s, cnt = 0, 0
for i in range(n):
    cnt += 1
    s += lst[i]
    if s > total / 2:
        break
print(cnt)
