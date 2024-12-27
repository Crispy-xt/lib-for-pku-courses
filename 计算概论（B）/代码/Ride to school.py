import math


def min_time(v, t):
    ari_ = (4.5 * 3600 / v) + t
    return ari_


ans = []
while True:
    lst = []
    n = int(input())
    if n != 0:
        for i in range(n):
            v, t = map(int, input().split())
            if t >= 0:
                lst.append(min_time(v, t))
        ans.append(min(lst))
    else:
        break
for answer in ans:
    print(math.ceil(answer))
