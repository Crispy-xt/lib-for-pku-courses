from collections import defaultdict
import heapq

def traversal(root,tree):
    lst=[root]+tree[root]
    lst.sort()
    for ele in lst:
        if ele==root:
            print(root)
        else:
            traversal(ele,tree)

tree=defaultdict(list)
s=set()
children=set()
for _ in range(int(input())):
    lst=list(map(int,input().split()))
    s.add(lst[0])
    if len(lst)>=2:
        for ele in lst[1:]:
            s.add(ele)
            children.add(ele)
            tree[lst[0]].append(ele)

root=(s-children).pop()
traversal(root,tree)





