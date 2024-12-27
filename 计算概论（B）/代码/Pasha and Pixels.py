a = 0
n, m, k = map(int, input().split())
set_ = set()
for t in range(k):
    i, j = map(int, input().split())
    pair = (i, j)
    set_.add(pair)
    if a == 0:
        if (
            ((i + 1, j) in set_ and (i, j + 1) in set_ and (i + 1, j + 1) in set_)
            or ((i - 1, j) in set_ and (i, j + 1) in set_ and (i - 1, j + 1) in set_)
            or ((i + 1, j) in set_ and (i, j - 1) in set_ and (i + 1, j - 1) in set_)
            or ((i - 1, j) in set_ and (i, j - 1) in set_ and (i - 1, j - 1) in set_)
        ):
            a = t + 1

print(a)
