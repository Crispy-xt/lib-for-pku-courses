def find_day(p, e, i, d):
    day = p % 23
    while (day - e) % 28 != 0:
        day += 23
    while (day - i) % 33 != 0:
        day += 23 * 28
    if (day - d) % 21252 == 0:
        return 21252
    else:
        return (day - d) % 21252


ans = []
while True:
    p, e, i, d = map(int, input().split())
    if p == e == i == d == -1:
        break
    else:
        ans.append(find_day(p, e, i, d))
for i, answer in enumerate(ans):
    print(f"Case {i+1}: the next triple peak occurs in {answer} days.")
