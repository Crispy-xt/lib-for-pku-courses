from collections import deque
n,k=map(int,input().split())
lst=[]
q=deque(list(range(1,n+1)))
m=1
while len(q)>1:
    num=q.popleft()
    if m==k:
        lst.append(num)
        m=1
    else:
        q.append(num)
        m+=1
print(' '.join(map(str,lst)))


