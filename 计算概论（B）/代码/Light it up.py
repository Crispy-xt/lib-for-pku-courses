from collections import deque

n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))
lst.append(m)
open_lst, close_lst = deque([]), deque([])
open, close = 0, 0
for i in range(n, -1, -1):
    if i % 2 == 0:
        open += lst[i + 1] - lst[i]
    else:
        close += lst[i + 1] - lst[i]
    open_lst.appendleft(open)
    close_lst.appendleft(close)

max_time = open_lst[0]
for i in range(1, n + 1):
    if i % 2 == 1 and lst[i + 1] > lst[i] + 1:
        max_time = max(max_time, open_lst[0] - open_lst[i] + close_lst[i] - 1)
    if i % 2 == 0 and i != n and lst[i + 1] > lst[i] + 1:
        max_time = max(max_time, open_lst[0] - open_lst[i + 1] + close_lst[i + 1] - 1)
print(max_time)
