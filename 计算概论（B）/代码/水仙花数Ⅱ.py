def judge(m):
    m=str(m)
    sum=0
    for i in range(len(m)):
        sum+=(int(m[i]))**3
    if sum==int(m):
        return True
    else:
        return False

lst=[]
a,b=map(int,input().split())
for i in range(a,b+1):
    if judge(i):
        lst.append(i)
length=len(lst)
if length==0:
    print("NO")
else:
    for i in range(length):
        if i!=length-1:
            print(lst[i],end=" ")
        else:
            print(lst[i])


