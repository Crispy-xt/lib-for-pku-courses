n = int(input())
price = sorted(list(map(int, input().split())))
max_price = price[-1]
choice = [0] * (max_price)
j = 0
for i in range(1, max_price):
    choice[i] = choice[i - 1]
    while i >= price[j]:
        choice[i] += 1
        j += 1
m = int(input())
ans = []
for _ in range(m):
    money = int(input())
    if money >= max_price:
        ans.append(n)
    else:
        ans.append(choice[money])
for answer in ans:
    print(answer)
