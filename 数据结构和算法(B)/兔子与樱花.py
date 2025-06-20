import heapq
from collections import defaultdict

def dijkstra(start, end):
    q = [(0, [start])]
    while q:
        distance, path = heapq.heappop(q)
        ver = path[-1]
        if ver == end:
            break
        for vertex, dist in graph[ver]:
            heapq.heappush(q, (distance + dist, path[:] + [vertex]))
    return path

p = int(input())
vertices = [input().strip() for _ in range(p)]
graph = defaultdict(list)
d = defaultdict(int)
for _ in range(int(input())):
    ver_1, ver_2, distance = input().split()
    distance = int(distance)
    graph[ver_1].append((ver_2, distance))
    graph[ver_2].append((ver_1, distance))
    d[(ver_1, ver_2)] = distance
    d[(ver_2, ver_1)] = distance
for _ in range(int(input())):
    start, end = input().split()
    path = dijkstra(start, end)
    for i in range(len(path) - 1):
        print(path[i], end="->")
        print(f"({d[(path[i],path[i+1])]})", end="->")
    print(path[-1])
