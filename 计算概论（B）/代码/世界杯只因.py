n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    lst[i]=(i-lst[i],i+lst[i])
lst.sort()
cnt=0
ll,rr=0,0
i=0
while i<n and ll<n:
    while i<n and lst[i][0]<=ll:
        rr=max(rr,lst[i][1])
        i+=1
    cnt+=1
    ll=rr+1
print(cnt)
        
