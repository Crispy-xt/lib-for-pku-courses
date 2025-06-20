from collections import deque


def topology_order(graph):
    degree_in = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            degree_in[v] += 1
    topo = []
    flag = True
    q = deque([u for u in graph if degree_in[u] == 0])
    while q:
        if len(q) != 1:
            flag = False
        u = q.popleft()
        for v in graph[u]:
            degree_in[v] -= 1
            if degree_in[v] == 0:
                q.append(v)
        topo.append(u)
    if len(topo) != len(graph):
        return -1
    return "".join(topo) if flag else 0


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    graph = {chr(ord("A") + k): [] for k in range(n)}
    edges = []
    for i in range(m):
        s = input()
        edges.append((s[0], s[-1]))

    for i in range(m):
        u, v = edges[i]
        graph[u].append(v)
        result = topology_order(graph)
        if result == -1:
            print(f"Inconsistency found after {i+1} relations.")
            break
        elif result != 0:
            print(f"Sorted sequence determined after {i+1} relations: {result}.")
            break
    else:
        print("Sorted sequence cannot be determined.")
