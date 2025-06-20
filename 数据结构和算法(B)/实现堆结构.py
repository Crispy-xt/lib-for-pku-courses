class Heap:
    def __init__(self):
        self.q=[0]
        self.size=0

    def percUp(self,i):
        while i//2>0:
            if self.q[i]<self.q[i//2]:
                self.q[i],self.q[i//2]=self.q[i//2],self.q[i]
            i//=2

    def insert(self,num):
        self.q.append(num)
        self.size+=1
        self.percUp(self.size)
    
    def minChild(self,i):
        if 2*i+1>self.size:
            return 2*i
        if self.q[2*i]<self.q[2*i+1]:
            return 2*i
        return 2*i+1
    
    def percDown(self,i):
        while 2*i<=self.size:
            k=self.minChild(i)
            if self.q[i]>self.q[k]:
                self.q[i],self.q[k]=self.q[k],self.q[i]
            i=k
    
    def popMin(self):
        self.q[1],self.q[self.size]=self.q[self.size],self.q[1]
        m=self.q.pop()
        self.size-=1
        self.percDown(1)
        return m

q=Heap()
for _ in range(int(input())):
    s=list(map(int,input().split()))
    if s[0]==1:
        q.insert(s[1])
    else:
        print(q.popMin())
    

    

    
    