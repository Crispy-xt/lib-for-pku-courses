n,m=map(int,input().split())
lst=[]
for _ in range(n):
    x,y=map(int,input().split())
    lst.append((x,y))
queue=[]
rr=0
cnt=0
for i in range(n):
    x,y=lst[i]
    if x>=rr:
        ll=max(rr,x-y+1)
        if ll+y<=m:
            cnt+=1
            rr=ll+y
            queue.append((ll,rr))
    elif x<rr-1:
        ll,rr=queue[-1]
        ll=max(ll,x-y+1)
        if ll+y<rr:
            queue.pop()
            queue.append((ll,ll+y))
            rr=ll+y
print(cnt)
        




