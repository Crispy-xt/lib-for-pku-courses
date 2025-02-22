def merge(a,b):
    c=[]
    i,j,cnt=0,0,0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
            cnt+=len(a)-i
    c.extend(a[i:])
    c.extend(b[j:])
    return c,cnt

def merge_sort(lst,ll,rr):
    if rr-ll<=1:
        return 0
    mid=(rr+ll)//2
    l_cnt=merge_sort(lst,ll,mid)
    r_cnt=merge_sort(lst,mid,rr)
    lst[ll:rr],cnt=merge(lst[ll:mid],lst[mid:rr])
    return l_cnt+cnt+r_cnt

ans=[]
while True:
    n=int(input())
    if n==0:
        break
    else:
        lst=[]
        for _ in range(n):
            lst.append(int(input()))
        ans.append(merge_sort(lst,0,n))
for answer in ans:
    print(answer)