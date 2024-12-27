def greedy(n):
    if n == 1 or n == 2:
        return 1
    if n == 4:
        return 3

    if n % 4 == 2:
        return n // 2 + greedy(n // 2 - 1)
    if n % 4 == 0:
        return n // 2 + greedy(n // 2 - 2)
    if n % 2 != 0:
        return 1 + (n - 1) - greedy(n - 1)


m = int(input())
ans = []
for _ in range(m):
    n = int(input())
    ans.append(greedy(n))
for answer in ans:
    print(answer)
