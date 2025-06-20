from collections import defaultdict


def dfs(x):
    visit[x] = 1
    for y, _ in graph[x]:
        if visit[y] == 1 or visit[y] == 0 and dfs(y):
            return True
    visit[x] = 2
    return False


def topology():
    while len(see) != n:
        lst = []
        for u in range(1, n + 1):
            if degree_in[u] == 0 and u not in see:
                lst.append(u)
                see.add(u)
        for u in lst:
            for v, _ in graph[u]:
                degree_in[v] -= 1
        topo.append(lst)


n, p = map(int, input().split())
degree_in = defaultdict(int)
degree_out = defaultdict(int)
graph = defaultdict(list)
activated = [False] * (n + 1)
visit = [0] * (n + 1)
topo = []
see = set()
neural = {}
for i in range(n):
    c, u = map(int, input().split())
    neural[i + 1] = c - u
for _ in range(p):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    degree_in[v] += 1
    degree_out[u] += 1

for x in range(1, n + 1):
    if visit[x] == 0 and dfs(x):
        print("NULL")
        exit()

out_layers = [u for u in range(1, n + 1) if degree_out[u] == 0]
layer = [u for u in range(1, n + 1) if degree_in[u] == 0]
topology()
layer = topo[0]
id = 0
topo.append([])
for u in layer:
    if neural[u] > 0:
        activated[u] = True
while layer:
    id += 1
    lst = set()
    for u in layer:
        if activated[u]:
            for v, w in graph[u]:
                lst.add(v)
                neural[v] += neural[u] * w
    for v in lst:
        if neural[v] > 0:
            activated[v] = True
    layer = topo[id]

flag = False

for u in sorted(out_layers):
    if activated[u]:
        print(u, neural[u])
        flag = True
if not flag:
    print("NULL")
