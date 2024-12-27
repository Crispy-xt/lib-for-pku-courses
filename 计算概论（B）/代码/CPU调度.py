n=int(input())
lst=[]
s=0
for _ in range(n):
    c,w=map(int,input().split())
    lst.append((w,c))
    s+=c
lst.sort(reverse=True)
t=0
m=0
for i in range(n):
    w,c=lst[i]
    t+=c
    s-=c
    m=max(m,t+s+max(0,w-s))
print(m)

