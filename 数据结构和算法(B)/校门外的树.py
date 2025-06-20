l,m=map(int,input().split())
Tree=[1]*(l+1)
for _ in range(m):
    a,b=map(int,input().split())
    for k in range(a,b+1):
        Tree[k]=0
print(sum(Tree))