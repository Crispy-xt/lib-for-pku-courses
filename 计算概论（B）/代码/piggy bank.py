def minimum_value(value, weight, gram):
    dp = [1000000] * (gram + 1)
    dp[0] = 0
    for i in range(1, gram + 1):
        for j in range(len(weight)):
            if weight[j] <= i:
                dp[i] = min(dp[i], dp[i - weight[j]] + value[j])
            else:
                break
    if dp[gram] == 1000000:
        return "This is impossible."
    else:
        return f"The minimum amount of money in the piggy-bank is {dp[gram]}."


result = []
for _ in range(int(input())):
    e, f = map(int, input().split())
    gram = f - e
    value, weight, lst = [], [], []
    for _ in range(int(input())):
        v, w = map(int, input().split())
        lst.append((w, v))
    lst.sort()
    for i in range(len(lst)):
        weight.append(lst[i][0])
        value.append(lst[i][1])
    result.append(minimum_value(value, weight, gram))
for ele in result:
    print(ele)
