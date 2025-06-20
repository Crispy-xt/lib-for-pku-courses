class disjointset():
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*(size)
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
    def connected(self,x,y):
        return self.find(x)==self.find(y)

for _ in range(int(input())):
    n,m=map(int,input().split())
    obj=disjointset(2*n)
    for _ in range(m):
        message,x,y=input().split()
        x,y=int(x)-1,int(y)-1
        if message=='D':
            obj.union(x,y+n)
            obj.union(x+n,y)
        else:
            if obj.connected(x,y):
                print('In the same gang.')
            elif obj.connected(x,y+n):
                print('In different gangs.')
            else:
                print('Not sure yet.')