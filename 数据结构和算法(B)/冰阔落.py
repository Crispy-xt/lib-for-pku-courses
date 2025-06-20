class disjointset():
    def __init__(self,size):
        self.parent=list(range(size))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x_root=self.find(x)
        y_root=self.find(y)
        if x_root==y_root:
            return
        else:
            self.parent[y_root]=x_root
    def is_connected(self,x,y):
        return self.find(x)==self.find(y)
    
while True:
    try:
        n,m=map(int,input().split())
        obj=disjointset(n)
        for _ in range(m):
            x,y=map(int,input().split())
            x-=1
            y-=1
            if obj.is_connected(x,y):
                print('Yes')
            else:
                obj.union(x,y)
                print('No')
        s=set(obj.find(x)+1 for x in range(n))
        l=len(s)
        print(l)
        print(' '.join(map(str,sorted(list(s)))))
    except EOFError:
        break