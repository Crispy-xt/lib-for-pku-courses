from collections import defaultdict
import heapq

n, m = map(int, input().split())
neighbors = defaultdict(list)
degree = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    degree[b] += 1
q = []
ans = []
s = set()
for _ in range(n):
    for node in range(1, n + 1):
        if degree[node] == 0 and node not in s:
            s.add(node)
            heapq.heappush(q, node)
    node=heapq.heappop(q)
    ans.append(node)
    for neighbor in neighbors[node]:
        degree[neighbor]-=1
for answer in ans:
    print(f"v{answer}", end=" ")
