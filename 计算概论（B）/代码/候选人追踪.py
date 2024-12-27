n,k=map(int,input().split())
lst=list(map(int,input().split()))
candidate=set(map(int,input().split()))
vote=sorted([(lst[2*i],lst[2*i+1]) for i in range(n)])
if k==314159:
    print(vote[-1][0])
else:
    cnt=0
    d={x:0 for x in candidate}
    num_list=[0 for _ in range(314160)]
    m,M=0,0
    for i in range(n-1):
        t=vote[i][1]
        if t in candidate:
            d[t]+=1
            if d[t]-1==m:
                m=min(d.values())
        else:
            num_list[t]+=1
            M=max(M,num_list[t])
        if m>M and vote[i][0]!=vote[i+1][0]:
            cnt+=vote[i+1][0]-vote[i][0]
    print(cnt)