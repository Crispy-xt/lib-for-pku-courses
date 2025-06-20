def can_reach(length,lst,k):
    cnt=0
    for ele in lst:
        cnt+=ele//length
    return cnt>=k

n,k=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))
l,r=1,10000
if not can_reach(1,lst,k):
    print(0)
else:
    while r-l>1:
        mid=(r+l)//2
        if can_reach(mid,lst,k):
            l=mid
        else:
            r=mid
    print(l)
