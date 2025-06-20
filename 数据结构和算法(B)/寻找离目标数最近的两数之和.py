target=int(input())
lst=list(map(int,input().split()))
lst.sort()
i,j=0,len(lst)-1
ans=float('inf')
flag=False
while i<j:
    s=lst[i]+lst[j]
    gap=abs(s-target)
    if s>target:
        if gap<ans:
            ans=gap
            flag=False
        j-=1
    elif s<target:
        if gap<=ans:
            ans=gap
            flag=True
        i+=1
    else:
        ans=0
        break
print(target-ans if flag else target+ans)  

