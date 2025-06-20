lst=sorted(list(map(float,input().split())))
n=len(lst)
m=int(n*0.4)
num=lst[m]
M=10**9
l,r=0,M
while r>l:
    mid=(r+l)//2
    score=mid*num/M+1.1**(num*mid/M)
    if score<85:
        l=mid+1
    else:
        r=mid
print(r)