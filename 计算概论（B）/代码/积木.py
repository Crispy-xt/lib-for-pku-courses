n=int(input())
s=[]
for _ in range(4):
    s.append(list(input()))
path=[]
lst=[]
used=[False for _ in range(4)]
def word(k):
    if len(path)==k:
        lst.append("".join(path))
        return
    for i in range(4):
        for j in range(6):
            if not used[i]:
                path.append(s[i][j])
                used[i]=True
                word(k)
                path.pop()
                used[i]=False
for k in range(1,5):
    word(k)
ans=[]
for _ in range(n):
    a=input()
    if a in lst:
        ans.append("YES")
    else:
        ans.append("NO")
for answer in ans:
    print(answer)

