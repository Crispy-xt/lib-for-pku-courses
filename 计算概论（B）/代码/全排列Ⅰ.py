def permutation(lst):
    n = len(lst)
    if n == 1:
        return [[lst[0]]]
    else:
        ans = []
        for i in range(0, n):
            new_lst = lst[:i] + lst[i + 1 :]
            for arr in permutation(new_lst):
                ans.append([lst[i]] + arr)
        return ans


n = int(input())
lst = list(range(1, n + 1))
for arr in permutation(lst):
    for i in range(n):
        if i != n - 1:
            print(arr[i], end=" ")
        else:
            print(arr[i])
