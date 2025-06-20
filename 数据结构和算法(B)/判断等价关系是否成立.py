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
            return
        elif self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            self.rank[y_root] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


obj = disjointset(26)
n = int(input())
check = []
for _ in range(n):
    s=input()
    x, y = s[0], s[-1]
    if s[1] == "=":
        obj.union(ord(x) - 97, ord(y) - 97)
    else:
        check.append((ord(x) - 97, ord(y) - 97))


for x, y in check:
    if obj.is_connected(x, y):
        print(False)
        exit()
print(True)


