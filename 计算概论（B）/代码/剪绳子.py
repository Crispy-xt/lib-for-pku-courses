import heapq
n=int(input())
queue=list(map(int,input().split()))
heapq.heapify(queue)
ans=0
while len(queue)>=2:
    a=heapq.heappop(queue)
    b=heapq.heappop(queue)
    ans+=(a+b)
    heapq.heappush(queue,a+b)
print(ans)
