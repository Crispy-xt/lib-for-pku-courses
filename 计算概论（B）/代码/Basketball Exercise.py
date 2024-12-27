n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
choose_lst = [1 if h1[0] >= h2[0] else 2]
dp_1, dp_2 = [0] * n, [0] * n
dp_1[0], dp_2[0] = h1[0], h2[0]
if n == 1:
    print(max(dp_1[0], dp_2[0]))
else:
    dp_1[1], dp_2[1] = h2[0] + h1[1], h1[0] + h2[1]
    for i in range(1, n):
        dp_1[i] = max(dp_2[i - 1] + h1[i], dp_1[i - 2] + h1[i], dp_2[i - 2] + h1[i])
        dp_2[i] = max(dp_1[i - 1] + h2[i], dp_2[i - 2] + h2[i], dp_1[i - 2] + h2[i])
    print(max(dp_1[-1], dp_2[-1]))
