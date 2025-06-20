n = int(input())
stack, lst, right, left = [], [], [n] * n, [-1] * n
ans = 0
for i in range(n):
    num = int(input())
    lst.append(num)
    while stack and num <= stack[-1][0]:
        _, id = stack.pop()
        right[id] = i
    stack.append((num, i))

stack = []
for i, x in enumerate(lst[::-1]):
    i = n - 1 - i
    while stack and x >= stack[-1][0]:
        _, id = stack.pop()
        left[id] = i
    stack.append((x, i))

id = 0
ans = 0
while id < n:
    r = right[id]
    rr = id + 1
    for j in range(r - 1, id, -1):
        if left[j] < id:
            ans = max(ans, j - id + 1)
            rr = j
            break
    id = rr

print(ans)
