m = int(input())
ans = []
for _ in range(m):
    lst = []
    n = int(input())
    for _ in range(n):
        s, d = map(int, input().split())
        lst.append((s, d))
    lst.sort()
    answer = 0
    while lst:
        s, d = lst.pop()
        answer += 1
        while lst and lst[-1][1] >= s:
            lst.pop()
    ans.append(answer)
for answer in ans:
    print(answer)
