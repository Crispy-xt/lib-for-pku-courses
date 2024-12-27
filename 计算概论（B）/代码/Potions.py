import heapq
n=int(input())
lst=list(map(int,input().split()))
health,cnt=0,0
queue=[]
for potion in lst:
    if health+potion>=0:
        health+=potion
        cnt+=1
        heapq.heappush(queue,potion)
    else:
        if queue and potion>queue[0]:
            m=heapq.heappop(queue)
            heapq.heappush(queue,potion)
            health=health-m+potion
print(cnt)
            
