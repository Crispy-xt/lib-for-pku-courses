n, k = map(int, input().split())
lst = list(map(int, input().split()))
i, j, cnt = 0, n - 1, 0
while i < j:
    if lst[i] + lst[j] < k:
        i += 1
    elif lst[i] + lst[j] > k:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1
print(cnt)
