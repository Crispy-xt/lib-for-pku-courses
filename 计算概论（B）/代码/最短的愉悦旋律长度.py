n,m=map(int,input().split())
lst=list(map(int,input().split()))
is_appear=[False for _ in range(10001)]
cnt=0
k=0
for i in range(n):
    if is_appear[lst[i]]==False:
        k+=1
        is_appear[lst[i]]=True
    if k==m:
        cnt+=1
        k=0
        is_appear=[False for _ in range(10001)]
print(cnt+1)


