n = int(input())
lst = []
for _ in range(n):
    x, h = map(int, input().split())
    lst.append((x, h))
lst.sort()
cnt = min(2, n)
fallen_direction = [0] * n
fallen_direction[0], fallen_direction[-1] = 1, 2
for i in range(1, n - 1):
    if fallen_direction[i - 1] == 0 or fallen_direction[i - 1] == 1:
        if lst[i][1] < lst[i][0] - lst[i - 1][0]:
            cnt += 1
            fallen_direction[i] = 1
        elif lst[i][1] < lst[i + 1][0] - lst[i][0]:
            cnt += 1
            fallen_direction[i] = 2
    else:
        if lst[i][1] < lst[i][0] - lst[i - 1][0] - lst[i - 1][1]:
            cnt += 1
            fallen_direction[i] = 1
        elif lst[i][1] < lst[i + 1][0] - lst[i][0]:
            cnt += 1
            fallen_direction[i] = 2
print(cnt)
