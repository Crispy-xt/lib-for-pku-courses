import heapq
n,m=map(int,input().split())
d={k:[] for k in range(1,n+1)}
for _ in range(m):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
q=[(0,1)]
max_gap=[float('inf')]*(n+1)
while q:
    gap,k=heapq.heappop(q)
    if gap>=max_gap[k]:
        continue
    max_gap[k]=gap
    if k==n:
        break
    for l,c in d[k]:
        if c+max_gap[k]<max_gap[l]:
            heapq.heappush(q,(c+max_gap[k],l))
print(max_gap[-1])
