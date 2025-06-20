class disjointset:
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0 for _ in range(size)]
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x_root=self.find(x)
        y_root=self.find(y)
        if x_root==y_root:
            return
        elif self.rank[x_root]>self.rank[y_root]:
            self.parent[y_root]=x_root
        elif self.rank[x_root]<self.rank[y_root]:
            self.parent[x_root]=y_root
        else:
            self.parent[x_root]=y_root
            self.rank[y_root]+=1

ans=[]
while True:
    n,m=map(int,input().split())
    if m==n==0:
        break
    obj=disjointset(n)
    for _ in range(m):
        lst=list(map(int,input().split()))
        lst=lst[1:]
        for i,member in enumerate(lst[:-1]):
            obj.union(member,lst[i+1])
    cnt=0
    root=obj.find(0)
    for i in range(n):
        if obj.find(i)==root:
            cnt+=1
    ans.append(cnt)
for answer in ans:
    print(answer)