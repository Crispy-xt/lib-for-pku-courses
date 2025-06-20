n, m, s, v = map(float, input().split())
n, m, s = int(n), int(m), int(s)
d = {k: [] for k in range(1, n + 1)}
for _ in range(m):
    a, b, r_ab, c_ab, r_ba, c_ba = map(float, input().split())
    a, b = int(a), int(b)
    d[a].append((b, r_ab, c_ab))
    d[b].append((a, r_ba, c_ba))

max_money = [-float("inf") for _ in range(n + 1)]
max_money[s] = v

for _ in range(n - 1):
    update = False
    for u in range(1, n + 1):
        if max_money[u] > 0:
            for v, r_uv, c_uv in d[u]:
                if max_money[u] > c_uv:
                    money = r_uv * (max_money[u] - c_uv)
                    if money > max_money[v] + 1e-12:
                        max_money[v] = money
                        update = True
    if not update:
        break

for u in range(1, n + 1):
    if max_money[u] > 0:
        for v, r_uv, c_uv in d[u]:
            if max_money[u] > c_uv:
                money = r_uv * (max_money[u] - c_uv)
                if money > max_money[v] + 1e-12:
                    print("YES")
                    exit()
print("NO")
