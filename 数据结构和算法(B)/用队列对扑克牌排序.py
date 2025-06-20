from collections import defaultdict

n = int(input())
pokers = list(input().split())
q = defaultdict(list)
for poker in pokers:
    num = poker[-1]
    q[num].append(poker)
lst = []
for char in "123456789":
    print(f"Queue{char}:", end="")
    print(" ".join(q[char]))
    for poker in q[char]:
        lst.append(poker)
for poker in lst:
    alpha = poker[0]
    q[alpha].append(poker)
lst = []
for char in "ABCD":
    print(f"Queue{char}:", end="")
    print(" ".join(q[char]))
    for poker in q[char]:
        lst.append(poker)
print(" ".join(lst))
