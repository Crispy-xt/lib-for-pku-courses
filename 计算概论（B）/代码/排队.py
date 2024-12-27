from collections import deque

ans = []
n, d = map(int, input().split())
height = deque(map(int, input().split()))
while height:
    lst = []
    max_val, min_val = height[0], height[0]
    for _ in range(len(height)):
        h = height.popleft()
        if abs(h - max_val) <= d and abs(h - min_val) <= d:
            lst.append(h)
        else:
            height.append(h)
        max_val = max(max_val, h)
        min_val = min(min_val, h)
    lst.sort()
    ans += lst

for ele in ans:
    print(ele, end=" ")
