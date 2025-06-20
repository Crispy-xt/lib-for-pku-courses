from collections import deque
def solve(n,m):
    q=deque([i for i in range(1,n+1)])
    for _ in range(n-1):
        cnt=1
        while cnt<=m:
            num=q.popleft()
            q.append(num)
            cnt+=1
        q.pop()
    return q[0]

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    else:
        print(solve(n,m))