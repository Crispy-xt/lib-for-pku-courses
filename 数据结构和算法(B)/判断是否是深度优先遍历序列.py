def check(graph, lst, n):
    visited = [False] * n
    stack = []
    for u in lst:
        while stack:
            v = stack[-1]
            if u in graph[v]:
                break
            for w in graph[v]:
                if not visited[w]:
                    return False
            stack.pop()
        stack.append(u)
        visited[u] = True
    return True


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
k = int(input())
for _ in range(k):
    lst = list(map(int, input().split()))
    print("YES" if check(graph, lst, n) else "NO")
