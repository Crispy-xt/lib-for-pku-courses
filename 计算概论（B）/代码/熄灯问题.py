path,lst=[],[]
def try_operation():
    if len(path)==6:
        lst.append(path[:])
        return
    for i in range(2):
        path.append(i)
        try_operation()
        path.pop()
    return lst
lst=try_operation()

matrix=[[0 for _ in range(8)]]
for _ in range(5):
    matrix.append([0]+list(map(int,input().split()))+[0])
matrix.append([0 for _ in range(8)])

for operation in lst:
    ans=[operation]
    m=[row[:] for row in matrix]
    for i in range(6):
        if operation[i]:
            m[1][i+1]=1-m[1][i+1]
            m[1][i]=1-m[1][i]
            m[1][i+2]=1-m[1][i+2]
            m[2][i+1]=1-m[2][i+1]
    for j in range(2,6):
        ans.append(m[j-1][1:7])
        for i in range(1,7):
            if m[j-1][i]:
                m[j-1][i]=1-m[j-1][i]
                m[j][i]=1-m[j][i]
                m[j][i-1]=1-m[j][i-1]
                m[j][i+1]=1-m[j][i+1]
                m[j+1][i]=1-m[j+1][i]
    if m[5][1:7]==[0,0,0,0,0,0]:
        break
for answer in ans:
    for ele in answer:
        print(ele,end=" ")
    print()