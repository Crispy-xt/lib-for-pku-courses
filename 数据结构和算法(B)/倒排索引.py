from collections import defaultdict
d=defaultdict(list)
n=int(input())
for i in range(1,n+1):
    s=set()
    lst=list(input().split())
    for ele in lst[1:]:
        if ele not in s:
            d[ele].append(i)
        s.add(ele)
for _ in range(int(input())):
    s=input()
    if d[s]:
        print(' '.join(map(str,d[s])))
    else:
        print('NOT FOUND')
