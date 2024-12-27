def min_stone(length, army):
    army.sort()
    army.append(10000)
    stone = 0
    while len(army) >= 2:
        n = len(army)
        start = army[0]
        for i in range(1, n):
            if army[i] - start > length:
                pos = i - 1
                stone += 1
                break
        for i in range(pos + 1, n):
            if army[i] - army[pos] > length:
                end = i - 1
                break
        army = army[(end + 1) :]
    return stone


stones = []
while True:
    r, n = map(int, input().split())
    if not (r == -1 and n == -1):
        army = list(map(int, input().split()))
        stones.append(min_stone(r, army))
    else:
        break
for stone in stones:
    print(stone)
