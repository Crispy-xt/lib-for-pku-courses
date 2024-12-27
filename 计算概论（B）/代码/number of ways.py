n = int(input())
lst = list(map(int, input().split()))
pre_sum = []
s = 0
for i in range(n):
    s += lst[i]
    pre_sum.append(s)
s /= 3
X, Y = [], []
cnt = 0
for i in range(n - 1):
    if pre_sum[i] == s * 2:
        Y.append(i)
        cnt += len(X)
    if pre_sum[i] == s:
        X.append(i)

print(cnt)
