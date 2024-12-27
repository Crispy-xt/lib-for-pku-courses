def can_place_radar(x, y, d):
    return (x - (d**2 - y**2) ** 0.5, x + (d**2 - y**2) ** 0.5)


def find_min_radar(lst):
    cnt = 1
    lst.sort()
    left = lst[0][0]
    right = lst[0][1]
    for i in range(len(lst)):
        if lst[i][0] <= right:
            right = min(right, lst[i][1])
        else:
            cnt += 1
            left = lst[i][0]
            right = lst[i][1]
    return cnt


ans = []
while True:
    judge = True
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    else:
        lst = []
        for i in range(n):
            x, y = map(int, input().split())
            if abs(y) > d:
                judge = False
            else:
                lst.append(can_place_radar(x, y, d))
        if judge:
            ans.append(find_min_radar(lst))
        else:
            ans.append(-1)
    m = input()
for i, answer in enumerate(ans):
    print(f"Case {i+1}: {answer}")
