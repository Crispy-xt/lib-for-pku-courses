def josephus(queue, m):
    lst = []
    if len(queue) == 1:
        lst.append(str(queue[0]))
        return lst
    else:
        for i in range(m):
            queue = queue[1:] + [queue[0]]
        lst.append(str(queue[-1]))
        del queue[-1]
        return lst + josephus(queue, m)


while True:
    n, p, m = map(int, input().split())
    if n == p == m == 0:
        break
    else:
        queue = list(range(p, n + 1)) + list(range(1, p))
        print(",".join(josephus(queue, m)))
