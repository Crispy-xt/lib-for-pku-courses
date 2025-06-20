from collections import defaultdict
import math
import heapq

x_1, y_1, x_2, y_2 = map(int, input().split())
v_foot, v_subway = 500 / 3, 2000 / 3
graph = defaultdict(list)
nodes = {(x_1, y_1), (x_2, y_2)}
while True:
    try:
        lst = list(map(int, input().split()))
        for i in range(0, len(lst) - 4, 2):
            x, y = lst[i], lst[i + 1]
            z, w = lst[i + 2], lst[i + 3]
            nodes.add((x, y))
            graph[(x, y)].append((z, w))
            graph[(z, w)].append((x, y))
        nodes.add((lst[-4], lst[-3]))
    except EOFError:
        break
min_time = {node: float("inf") for node in nodes}
q = [(0, x_1, y_1)]
while q:
    t, x, y = heapq.heappop(q)
    if t >= min_time[(x, y)]:
        continue
    min_time[(x, y)] = t
    for node in nodes:
        z, w = node
        if min_time[node] > t:
            d = math.sqrt((x - z) ** 2 + (y - w) ** 2)
            if node in graph[(x, y)]:
                heapq.heappush(q, (t + d / v_subway, z, w))
            else:
                heapq.heappush(q, (t + d / v_foot, z, w))
ans = min_time[(x_2, y_2)]
ans = int(ans) + int(2 * (ans - int(ans)))
print(ans)
