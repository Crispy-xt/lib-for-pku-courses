from collections import deque, defaultdict

id = defaultdict(int)
t = int(input())
for i in range(t):
    for m in list(map(int, input().split())):
        id[m] = i
group = deque()
q = defaultdict(deque)
lst = []
while True:
    command = input()
    if command == "STOP":
        break
    elif command == "DEQUEUE":
        m = q[group[0]].popleft()
        lst.append(m)
        if not q[group[0]]:
            group.popleft()
    else:
        _, m = command.split()
        m = int(m)
        if id[m]:
            if not q[id[m]]:
                group.append(id[m])
            q[id[m]].append(m)
        else:
            id[m] = t
            t += 1
            group.append(id[m])
            q[id[m]].append(m)
for m in lst:
    print(m)
