queue=[]
n=int(input())
a,b=map(int,input().split())
s=a
for _ in range(n):
    x,y=map(int,input().split())
    queue.append((x*y,x))
    s*=x
queue.sort()
s//=queue[-1][0]
print(s)
