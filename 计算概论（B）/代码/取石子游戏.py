ans=[]
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    else:
        flag=True
        while True:
            c,d=max(a,b),min(a,b)
            if c//d>=2:
                if flag:
                    ans.append("win")
                    break
                else:
                    ans.append("lose")
                    break
            else:
                if c==d:
                    if flag:
                        ans.append("win")
                        break
                    else:
                        ans.append("lose")
                        break
                else:
                    a,b=c-d,d
                    flag=not flag
for answer in ans:
    print(answer)
