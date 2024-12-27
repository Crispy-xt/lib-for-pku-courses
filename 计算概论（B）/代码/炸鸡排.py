n, k = map(int, input().split())
lst = list(map(int, input().split()))
s = sum(lst)
lst.sort()
while lst[-1] > s / k:
    s -= lst[-1]
    lst.pop()
    k -= 1
print(f"{s/k:.3f}")
