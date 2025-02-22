n,m=map(int,input().split())
lst=list(map(int,input().split()))
for _ in range(m):
    s,i=input().split()
    i=int(i)
    if s=='C':
        for k in range(n):
            lst[k]=(lst[k]+i)%65536
    else:
        cnt=0
        for ele in lst:
            if (ele>>i) & 1:
                cnt+=1
        print(cnt)

