class disjointset:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1
        return True


n = int(input())
obj = disjointset(n)
edge = []
for _ in range(n - 1):
    lst = list(input().split())
    u = lst[0]
    while len(lst) > 2:
        dist = lst.pop()
        v = lst.pop()
        edge.append((int(dist), ord(u) - 65, ord(v) - 65))
ans, cnt = 0, 0
edge.sort()
for dist, u, v in edge:
    if obj.union(u, v):
        ans += dist
        cnt += 1
    if cnt == n - 1:
        break
print(ans)
