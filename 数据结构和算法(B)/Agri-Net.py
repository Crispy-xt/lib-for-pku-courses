import heapq
while True:
    try:
        n = int(input())
        distance = []
        for _ in range(n):
            distance.append(list(map(int, input().split())))
        visited = [False] * n
        visited[0] = True
        q=[]
        mst = []
        for v in range(1, n):
            heapq.heappush(q, (distance[0][v], v))
        while len(mst) < n - 1:
            dist, u = heapq.heappop(q)
            if not visited[u]:
                visited[u] = True
                mst.append(dist)
                for v in range(n):
                    if v != u and not visited[v]:
                        heapq.heappush(q, (distance[u][v], v))
        print(sum(mst))
    except EOFError:
        break
