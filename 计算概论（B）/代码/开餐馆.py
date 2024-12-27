from collections import defaultdict

ans = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    pos = list(map(int, input().split()))
    profit = list(map(int, input().split()))
    dict = defaultdict(int)
    for i in range(n):
        dict[pos[i]] = profit[i]
        for j in range(i):
            if pos[j] + k < pos[i]:
                dict[pos[i]] = max(dict[pos[i]], dict[pos[j]] + profit[i])
    max_profit = max(dict.values())
    ans.append(max_profit)
for answer in ans:
    print(answer)
