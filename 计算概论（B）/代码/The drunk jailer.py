def opened(n):
    lst=[0]*(n+1)
    open_door=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j%i==0:
                lst[j]+=1
    for ele in lst:
        if ele%2==1:
            open_door+=1
    return (open_door)

n=int(input())
for _ in range(n):
    m=int(input())
    print(opened(m))
