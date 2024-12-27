from collections import deque

n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
queue = deque()
for i in range(n):
    while queue and lst[queue[-1]] <= lst[i]:
        queue.pop()
    queue.append(i)
    if i - queue[0] >= k:
        queue.popleft()
    if i >= k - 1:
        ans.append(lst[queue[0]])
for answer in ans:
    print(answer, end=" ")
