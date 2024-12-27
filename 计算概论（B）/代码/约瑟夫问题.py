def jusephus(lst,m):
    n=len(lst)
    if n==1:
        return lst[0]
    else:
        r=(m-1)%n
        lst.pop(r)
        return jusephus(lst[r:]+lst[0:r],m)

while True:
    n,m=map(int,input().split())
    if (m+n)!=0:
        lst=list(range(1,n+1))
        print(jusephus(lst,m))
    else:
        break