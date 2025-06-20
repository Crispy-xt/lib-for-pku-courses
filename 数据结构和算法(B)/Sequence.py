import heapq

def marge(a,b,n):
    q,result=[],[]
    visited=set()
    i,j=0,0
    heapq.heappush(q,(a[0]+b[0],0,0))
    while len(result)<n and q:
        s,i,j=heapq.heappop(q)
        result.append(s)
        if j+1<len(b) and (i,j+1) not in visited:
            heapq.heappush(q,(a[i]+b[j+1],i,j+1))
            visited.add((i,j+1))
        if i+1<len(a) and (i+1,j) not in visited:
            heapq.heappush(q,(a[i+1]+b[j],i+1,j))
            visited.add((i+1,j))
    return result

for _ in range(int(input())):
    mat=[]
    m,n=map(int,input().split())
    for _ in range(m):
        mat.append(sorted(list(map(int,input().split())))[:n])
    while len(mat)>=2:
        a=mat.pop()
        b=mat.pop()
        mat.append(marge(a,b,n))
    print(' '.join(map(str,mat[0])))

