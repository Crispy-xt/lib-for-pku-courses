def max_nonoverlapping(lst):
    n = len(lst)
    cnt = 0
    suffix_sum = set([0])
    s = 0
    for i in range(len(lst) - 1, -1, -1):
        s += lst[i]
        if s in suffix_sum:
            cnt += 1
            s = 0
            suffix_sum = set([0])
        suffix_sum.add(s)
    return cnt


t = int(input())
result = []
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    result.append(max_nonoverlapping(lst))
for ele in result:
    print(ele)
