a,b,c=[],[],[]
m1,n1=map(int,input().split())
for _ in range(m1):
    a.append(list(map(int,input().split())))
m2, n2 = map(int,input().split())
for _ in range(m2):
    b.append(list(map(int, input().split())))
m3, n3 = map(int,input().split())
for _ in range(m3):
    c.append(list(map(int, input().split())))
if n1==m2 and m1==m3 and n2==n3:
    for i in range(m3):
        for j in range(n3):
            for k in range(n1):
                c[i][j]+=a[i][k]*b[k][j]
    for row in c:
        print(' '.join(map(str,row)))
else:
    print('Error!')
