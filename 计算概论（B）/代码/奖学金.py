def compare(x, y):
    if x[0] > y[0]:
        return True
    elif x[0] < y[0]:
        return False
    else:
        if x[1] > y[1]:
            return True
        elif x[1] < y[1]:
            return False
        else:
            if x[2] < y[2]:
                return True
            else:
                return False


n = int(input())
lst = []
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    s = a + b + c
    lst.append((s, a, i))
for i in range(n):
    for j in range(i + 1, n):
        if not compare(lst[i], lst[j]):
            c = lst[i]
            lst[i] = lst[j]
            lst[j] = c
for i in range(5):
    print(lst[i][-1], lst[i][0])
