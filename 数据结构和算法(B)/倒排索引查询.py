from collections import defaultdict

doc_set = set()
n = int(input())
d = defaultdict(list)
for i in range(n):
    lst = list(map(int, input().split()))
    for ele in lst[1:]:
        d[i].append(ele)
        doc_set.add(ele)

m = int(input())
for i in range(m):
    lst = list(map(int, input().split()))
    s = doc_set
    for i, ele in enumerate(lst):
        if ele == 1:
            s = s & set(d[i])
        elif ele == -1:
            s = s - set(d[i])
    if s:
        s = list(s)
        s.sort()
        print(" ".join(map(str, s)))
    else:
        print("NOT FOUND")
