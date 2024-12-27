n=int(input())
lst=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a>=0 and b<=60:
        lst.append((a,b))
lst.sort(reverse=True)
left=lst[0][0]
cnt=1
for i in range(n):
    if lst[i][1]<left:
        cnt+=1
        left=lst[i][0]
print(cnt)
