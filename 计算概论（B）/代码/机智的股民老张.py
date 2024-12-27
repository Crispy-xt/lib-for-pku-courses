lst = list(map(int, input().split()))
max_earn = 0
min_in = float("inf")
for i in range(len(lst)):
    if lst[i] < min_in:
        min_in = lst[i]
    max_earn = max(max_earn, lst[i] - min_in)
print(max_earn)
