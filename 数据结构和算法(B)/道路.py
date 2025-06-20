from collections import defaultdict
import heapq

k = int(input())
n = int(input())
neighbors = defaultdict(list)
for _ in range(int(input())):
    start, end, distance, cost = map(int, input().split())
    neighbors[start].append((end, distance, cost))
q = [(0, 0, 1)]
flag = False
while q:
    dist, spend, city = heapq.heappop(q)
    if city == n:
        flag = True
        break
    for neighbor, distance, cost in neighbors[city]:
        if spend + cost <= k:
            heapq.heappush(q, (dist + distance, spend + cost, neighbor))
print(dist if flag else -1)
