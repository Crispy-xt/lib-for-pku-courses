import heapq
n=int(input())
q=list(map(int,input().split()))
heapq.heapify(q)
s=0
while len(q)>=2:
    a=heapq.heappop(q)
    b=heapq.heappop(q)
    heapq.heappush(q,a+b)
    s+=(a+b)
print(s)