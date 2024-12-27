n = int(input())
ans = []
for _ in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    ans.append(min(min_a * k + sum(b), min_b * k + sum(a)))
for answer in ans:
    print(answer)
