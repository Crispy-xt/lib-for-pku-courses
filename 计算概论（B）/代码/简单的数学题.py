def log(n):
    if n==1:
        return 0
    else:
        for i in range(1,n):
            if 2**i<=n<2**(i+1):
                return i
def cal(n):
    m=log(n)
    s=n*(n+1)//2
    s-=(2**(m+2)-2)
    return s

n=int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(cal(a))
for answer in ans:
    print(answer)
    