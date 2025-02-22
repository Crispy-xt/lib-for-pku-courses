import heapq
q=[]
for _ in range(int(input())):
    s=input()
    if s[0]=='1':
        _,num=s.split()
        num=int(num)
        heapq.heappush(q,num)
    else:
        num=heapq.heappop(q)
        print(num)