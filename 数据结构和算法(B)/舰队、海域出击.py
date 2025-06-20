from collections import defaultdict


def find_cycle(n, degree, neighbors):
    see = set()
    while len(see) < n:
        flag = False
        for i in range(1, n + 1):
            if degree[i] == 0 and i not in see:
                see.add(i)
                flag = True
                for neighbor in neighbors[i]:
                    degree[neighbor] -= 1
        if not flag:
            return True
    return False


for _ in range(int(input())):
    n, m = map(int, input().split())
    degree = defaultdict(int)
    neighbors = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        degree[b] += 1
        neighbors[a].append(b)
    print("Yes" if find_cycle(n, degree, neighbors) else "No")
