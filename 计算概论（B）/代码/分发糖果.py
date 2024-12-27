n=int(input())
ratings=list(map(int,input().split()))
l,r=[1 for _ in range(n)],[1 for _ in range(n)]
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        l[i]=l[i-1]+1
for i in range(n-1,0,-1):
    if ratings[i-1]>ratings[i]:
        r[i-1]=r[i]+1
s=0
for i in range(n):
    s+=max(l[i],r[i])
print(s)
