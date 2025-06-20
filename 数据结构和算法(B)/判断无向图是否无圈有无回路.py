class disjointset():
    def __init__(self,size):
        self.parents=list(range(size))
        self.rank=[0]*size
    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    def union(self,x,y):
        x_root,y_root=self.find(x),self.find(y)
        if x_root==y_root:
            return
        elif self.rank[x_root]<self.rank[y_root]:
            self.parents[x_root]=y_root
        elif self.rank[x_root]>self.rank[y_root]:
            self.parents[y_root]=x_root
        else:
            self.parents[x_root]=y_root
            self.rank[x_root]+=1
    def is_connected(self,x,y):
        return self.find(x)==self.find(y)
    
n,m=map(int,input().split())
obj=disjointset(n)
flag=False
for _ in range(m):
    x,y=map(int,input().split())
    if obj.is_connected(x,y):
        flag=True
    obj.union(x,y)
s=len(set(obj.find(x) for x in range(n)))
if s==1:
    print('connected:yes')
else:
    print('connected:no')
print('loop:yes' if flag else 'loop:no')

