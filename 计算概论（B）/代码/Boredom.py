from collections import defaultdict

n = int(input())
lst = sorted(list(map(int, input().split())))
dict = defaultdict(int)
for ele in lst:
    dict[ele] += 1
dp = [0] * len(dict)
key = list(dict.keys())
dp[0] = key[0] * dict[key[0]]
if len(dict) == 1:
    print(dp[0])

else:
    used = [False] * len(dict)
    used[0] = True
    for i in range(1, len(dict)):
        if i >= 2:
            dp[i] = dp[i - 2] + key[i] * dict[key[i]]
        if key[i] == key[i - 1] + 1 and used[i - 1]:
            if key[i] * dict[key[i]] > key[i - 1] * dict[key[i - 1]]:
                used[i] = True
                dp[i] = max(
                    dp[i],
                    dp[i - 1] + key[i] * dict[key[i]] - key[i - 1] * dict[key[i - 1]],
                )
            else:
                if dp[i] <= dp[i - 1]:
                    dp[i] = dp[i - 1]
                else:
                    used[i] = True
        else:
            dp[i] = max(dp[i], dp[i - 1] + key[i] * dict[key[i]])
            used[i] = True
    print(dp[-1])
