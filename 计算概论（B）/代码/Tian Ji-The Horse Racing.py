from collections import deque


def race_strategy(tianji, opponent):
    win_gold = 0
    while tianji:
        if (
            tianji[0] < opponent[0] or tianji[-1] < opponent[-1]
        ):  # tianji的最差的马必输/opponent的最好的马必胜
            tianji.popleft()
            opponent.pop()
            win_gold -= 200
        else:
            if tianji[-1] > opponent[-1]:  # tianji最好的马必胜
                tianji.pop()
                opponent.pop()
                win_gold += 200
            elif tianji[0] > opponent[0]:  # opponent最坏的马必输
                tianji.popleft()
                opponent.popleft()
                win_gold += 200
            else:  # tianji和opponent最好最坏的马都一样
                a = tianji.popleft()
                b = opponent.pop()
                if a < b:
                    win_gold -= 200
    return win_gold


ans = []
while True:
    n = int(input())
    if n != 0:
        tianji, opponent = deque([]), deque([])
        lst_1 = sorted(list(map(int, input().split())))
        lst_2 = sorted(list(map(int, input().split())))
        tianji.extend(lst_1)
        opponent.extend(lst_2)
        ans.append(race_strategy(tianji, opponent))
    else:
        break
for answer in ans:
    print(answer)
