def trans(n, k):
    digit = "0123456789ABCDEF"
    lst = []
    while n >= 1:
        lst.append(digit[n % k])
        n = n // k
    return "".join(lst[::-1])


n, k = map(int, input().split())
print(trans(n, k))
