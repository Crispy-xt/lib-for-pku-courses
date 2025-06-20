def merge(a,b):
    c,cnt,i,j=[],0,0,0
    while i<len(a) and j<len(b):
        if a[i]>=b[j]:
            c.append(b[j])
            j+=1
            cnt+=len(a)-i
        else:
            c.append(a[i])
            i+=1
    c.extend(a[i:])
    c.extend(b[j:])
    return c,cnt

def merge_sort(lst,ll,rr):
    if rr-ll<=1:
        return 0
    mid=(ll+rr)//2
    l_cnt=merge_sort(lst,ll,mid)
    r_cnt=merge_sort(lst,mid,rr)
    lst[ll:rr],cnt=merge(lst[ll:mid],lst[mid:rr])
    return l_cnt+r_cnt+cnt

lst=[]
n=int(input())
for _ in range(n):
    lst.append(int(input()))
cnt=merge_sort(lst,0,n)
print(n*(n-1)//2-cnt)