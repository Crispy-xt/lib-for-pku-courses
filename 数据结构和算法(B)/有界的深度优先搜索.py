def dfs(u, l, k):
    if k == l:
        return
    for v in graph[u]:
        if not visited[v]:
            ans.append(v)
            visited[v] = True
            dfs(v, l, k + 1)


n, m, l = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n):
    graph[i].sort()
visited = [False] * n
u = int(input())
ans = [u]
visited[u] = True
dfs(u, l, 0)
print(" ".join(map(str, ans)))
