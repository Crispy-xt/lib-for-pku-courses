from collections import deque

while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    q=deque(range(n))
    ans=[]
    for i in range(1,m*n+1):
        num=q.popleft()
        if i%m!=0:
            q.append(num)
        else:
            num=(num+p-1)%n+1
            ans.append(str(num))
    print(','.join(ans))


