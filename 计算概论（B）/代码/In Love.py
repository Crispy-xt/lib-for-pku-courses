from collections import defaultdict
import heapq

ans=[]
d_l,d_r=defaultdict(int),defaultdict(int)
n=int(input())
max_l,min_r=[],[]
for _ in range(n):
    s,l,r=input().split()
    l,r=int(l),int(r)
    if s=='+':
        d_l[l]+=1
        heapq.heappush(max_l,-l)
        d_r[r]+=1
        heapq.heappush(min_r,r)
    else:
        d_l[l]-=1
        d_r[r]-=1
    while max_l and d_l[-max_l[0]]==0:
        heapq.heappop(max_l)
    while min_r and d_r[min_r[0]]==0:
        heapq.heappop(min_r)
    if max_l and min_r and min_r[0]<-max_l[0]:
        ans.append('YES')
    else:
        ans.append('NO')
for answer in ans:
    print(answer)
    
    

