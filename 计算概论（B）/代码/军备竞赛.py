from collections import deque
import sys

p = int(input())
number = input()
lst = list(map(int, number.split()))
lst.sort()
lst = deque(lst)
ans = 0
if p < lst[0]:
    print(ans)
    sys.exit()
while lst:
    if p >= lst[0]:
        p -= lst[0]
        lst.popleft()
        ans += 1
    elif len(lst) >= 2:
        p += lst[-1]
        lst.pop()
        ans -= 1
    else:
        break
print(ans)
