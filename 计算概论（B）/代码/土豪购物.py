def get_min(lst):
    m=[0]
    n=len(lst)
    for i in range(n):
        if lst[i]<m[-1]:
            m.append(lst[i])
        else:
            m.append(m[-1])
    return m
def get_max(lst):
    n=len(lst)
    M=[lst[-1]]
    for i in range(2,n+1):
        if lst[-i]>M[-1]:
            M.append(lst[-i])
        else:
            M.append(M[-1])
    return M[::-1]

lst=list(input().split(","))
n=len(lst)
for i in range(n):
    lst[i]=int(lst[i])
if any(x>=0 for x in lst):
    pre_sum=[lst[0]]
    for i in range(1,n):
        pre_sum.append(pre_sum[-1]+lst[i])
    ans=pre_sum[-1]
    m=get_min(pre_sum)
    M=get_max(pre_sum)
    for i in range(n):
        ans=max(ans,M[i]-m[i]-lst[i],M[i]-m[i])
    print(ans)
else:
    print(max(lst))

