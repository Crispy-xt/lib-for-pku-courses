from collections import deque


def bfs(m, n):
    seen = set()
    queue = deque([(m, [])])
    while deque:
        m, lst = queue.popleft()
        if m == n:
            return lst
        cnt=0
        seen.add(m)
        if m * 3 not in seen:
            queue.append((m * 3, lst + ["H"]))
            seen.add(m*3)
        if m // 2 not in seen:
            queue.append((m // 2, lst + ["O"]))
            seen.add(m//2)


ans = []
while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    else:
        lst = bfs(m, n)
        ans.append((len(lst), lst))
for k, answer in ans:
    print(k, end="\n")
    print("".join(answer))
