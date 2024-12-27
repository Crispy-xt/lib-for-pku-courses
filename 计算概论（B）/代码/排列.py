def find_next_permutation(lst):
    n = len(lst)
    flag = False
    if lst == list(range(n, 0, -1)):
        return list(range(1, n + 1))
    else:
        for pos in range(n - 1, 0, -1):
            if lst[pos] > lst[pos - 1]:
                for j in range(pos, n):
                    if lst[j] < lst[pos - 1]:
                        lst[j - 1], lst[pos - 1] = lst[pos - 1], lst[j - 1]
                        flag = True
                        break
                if not flag:
                    lst[-1], lst[pos - 1] = lst[pos - 1], lst[-1]
                break
        return lst[: pos - 1] + [lst[pos - 1]] + lst[n - 1 : pos - 1 : -1]


m = int(input())
ans = []
for _ in range(m):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(k):
        lst = find_next_permutation(lst)
    ans.append(lst)
for lst in ans:
    for ele in lst:
        print(ele, end=" ")
    print()
