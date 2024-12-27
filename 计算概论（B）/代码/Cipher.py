def cycle_k_lst(lst, n, k):
    lst_k = [0] * n
    cycle_lst = [0] * n
    is_cycle = [False] * n
    for i in range(n):
        if not is_cycle[i]:
            visited = [i]
            is_cycle[i] = True
            x = lst[i]
            cycle = 1
            while x != i + 1:
                visited.append(x - 1)
                is_cycle[x - 1] = True
                x = lst[x - 1]
                cycle += 1
            for pos in visited:
                cycle_lst[pos] = cycle
    for i in range(n):
        f_times = k % cycle_lst[i]
        if f_times == 0:
            lst_k[i] = i + 1
        else:
            x = lst[i]
            for _ in range(f_times - 1):
                x = lst[x - 1]
            lst_k[i] = x
    return lst_k


def trans(code, lst, n, k):
    l = len(code)
    code = code + (" " * (n - l))
    tran_lst = [" "] * n
    lst_k = cycle_k_lst(lst, n, k)
    for i in range(n):
        tran_lst[lst_k[i] - 1] = code[i]
    return "".join(tran_lst)


ans = []
while True:
    n = int(input())
    if n != 0:
        lst = list(map(int, input().split()))
        while True:
            s = input()
            if s != "0":
                k, code = s.split(" ", 1)
                k = int(k)
                ans.append(trans(code, lst, n, k))
            else:
                ans.append("\r")
                break
    else:
        break
for answer in ans:
    print(answer)
