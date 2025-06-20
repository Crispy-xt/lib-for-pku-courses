class disjointset():
    def __init__(self,size):
        self.parent=list(range(size+1))
        self.rank=[0 for _ in range(size+1)]
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        xset=self.find(x)
        yset=self.find(y)
        if xset==yset:
            return
        elif self.rank[xset]>self.rank[yset]:
            self.parent[yset]=xset
        elif self.rank[xset]<self.rank[yset]:
            self.parent[xset]=yset
        else:
            self.parent[xset]=yset
            self.rank[yset]+=1
    def connected(self,x,y):
        return self.find(x)==self.find(y)

ans=[]
while True:
    n,m=map(int,input().split())  
    if m==n==0:
        break  
    obj=disjointset(n)
    for _ in range(m):
        x,y=map(int,input().split()) 
        obj.union(x,y)
    ans.append(len(set(obj.find(x) for x in range(1,n+1))))

for i,answer in enumerate(ans):
    print(f"Case {i+1}: {answer}")
