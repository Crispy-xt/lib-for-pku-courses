import bisect
def can_reach(spend):
    id=1
    cnt=0
    while id<=n:
        next_id=bisect.bisect_right(pre_sum,spend+pre_sum[id-1])
        cnt+=1
        id=next_id
    return cnt<=m


n,m=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))

pre_sum=[0,lst[0]]
for i in range(1,n):
    pre_sum.append(pre_sum[-1]+lst[i])

ll=max(lst)-1
rr=pre_sum[-1]
if m==n:
    print(ll)
elif m==1:
    print(rr)
else:
    while rr-ll>1:
        mid=(ll+rr)//2
        if can_reach(mid):
            rr=mid
        else:
            ll=mid
    print(rr)


