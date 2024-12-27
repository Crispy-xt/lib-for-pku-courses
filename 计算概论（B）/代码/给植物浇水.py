n,a,b=map(int,input().split())
plant=list(map(int,input().split()))
i,j=0,n-1
cnt=0
x,y=a,b
if n==1:
    if max(a,b)>=plant[0]:
        print(0)
    else:
        print(1)
elif n==2:
    if a<plant[0]:
        cnt+=1
    if b<plant[1]:
        cnt+=1
    print(cnt)
else:
    while i<j-1:
        if x>=plant[i]:
            x-=plant[i]
            i+=1
        else:
            x=a
            x-=plant[i]
            i+=1
            cnt+=1
        if y>=plant[j]:
            y-=plant[j]
            j-=1
        else:
            y=b
            y-=plant[j]
            j-=1
            cnt+=1
    if i==j:
        if max(x,y)<plant[i]:
            cnt+=1
    else:
        if x<plant[i]:
            cnt+=1
        if y<plant[j]:
            cnt+=1
    print(cnt)
