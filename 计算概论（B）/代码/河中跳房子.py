import bisect

l,n,m=map(int,input().split())
lst=[0]
for _ in range(n):
    lst.append(int(input()))
lst.append(l)

def can_reach(t):
    cnt,i=0,0
    while i<=n:
        j=bisect.bisect_left(lst,lst[i]+t)
        cnt+=j-i-1
        i=j
    if cnt<=m:
        return True
    return False
if m==n:
    print(l)
else:
    gap=sorted([lst[i + 1] - lst[i] for i in range(n + 1)])
    start=gap[m-1]
    end=l
    while end-start>1:
        i=(end+start)//2
        if can_reach(i):
            start=i
        else:
            end=i
    print(start)