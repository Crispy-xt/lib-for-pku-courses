x=input()
m="hello"
for i in x:
    if i==m[0]:
        m=m[1:]
    if m== "":
        print("YES")
        break
else:
    print("NO")
