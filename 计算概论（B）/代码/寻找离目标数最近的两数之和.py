target = int(input())
lst = sorted(list(map(int, input().split())))
n = len(lst)
i, j = 0, n - 1
m, sign = lst[i] + lst[j], lst[i] + lst[j] - target
while j - i > 1:
    if sign < 0 and j - i > 1:
        i += 1
        sign = lst[i] + lst[j] - target
    else:
        j -= 1
        sign = lst[i] + lst[j] - target
    if abs(m - target) > abs(sign):
        m = sign + target
    elif abs(m - target) == abs(sign) and sign < 0:
        m = sign + target
print(m)
