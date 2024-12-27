h = int(input())
m = int(input())
lst = []
for _ in range(m):
    a, b = map(float, input().split())
    lst.append((a * b, a))
lst.sort(reverse=True)
h = 2 * h - 0.5 * m
gpa = 0
for i in range(m):
    if h > 0:
        t = min(h, 5 / lst[i][1])
        h -= t
        gpa += t * lst[i][0]
print("{:.1f}".format(gpa))
