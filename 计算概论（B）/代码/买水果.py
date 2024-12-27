from collections import defaultdict

n, m = map(int, input().split())
value = sorted(map(int, input().split()))
d = defaultdict(int)
a = set()
for _ in range(m):
    s = input()
    d[s] += 1
    a.add(s)
lst = []
for s in a:
    lst.append(d[s])
lst.sort()
m, M = 0, 0
for i in range(len(lst)):
    m += value[i] * lst[-i - 1]
value = value[::-1]
for i in range(len(lst)):
    M += value[i] * lst[-i - 1]
print(m, M)
