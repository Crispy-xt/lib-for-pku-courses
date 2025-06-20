n, m = map(int, input().split())
neighbors, parents = {k: [] for k in range(n)}, {k: [] for k in range(n)}
degree = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    parents[b].append(a)
    degree[b] += 1
see = set()
ans = 100 * n
topology_order = []
while len(topology_order) < n:
    lst = []
    for u in range(n):
        if degree[u] == 0 and u not in topology_order:
            lst.append(u)
    for u in lst:
        topology_order.append(u)
        for v in neighbors[u]:
            degree[v] -= 1
dp = [0] * n
for u in topology_order[::-1]:
    for v in parents[u]:
        if dp[v] <= dp[u]:
            dp[v] = dp[u] + 1

ans += sum(dp)
print(ans)
