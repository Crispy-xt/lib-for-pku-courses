n,capacity=map(int,input().split())
value=[]
w=0
for _ in range(n):
    a,b=map(int,input().split())
    w+=b
    for _ in range(b):
        value.append(a/b)
value.sort(reverse=True)
sum=0
for i in range(min(w,capacity)):
    sum+=value[i]
print(sum)



