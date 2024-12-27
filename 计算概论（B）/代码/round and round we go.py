def is_round(num):
    n = len(num)
    r = int(num)
    flag = [False] * n
    for i in range(n):
        s = int(num[i:] + num[:i])
        if s / r != int(s / r) or s / r > n:
            return False
        else:
            flag[int(s / r) - 1] = True
    for i in range(n):
        if not flag[i]:
            return False
    return True


while True:
    try:
        num = input()
        if is_round(num):
            print(f"{num} is cyclic")
        else:
            print(f"{num} is not cyclic")
    except EOFError:
        break
