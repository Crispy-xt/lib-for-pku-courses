s=input()
stack=[]
ans=''
for char in s:
    if char=='[':
        stack.append([0,''])
    elif char.isdigit():
        stack[-1][0]=stack[-1][0]*10+int(char)
    elif char==']':
        multi,res=stack.pop()
        res*=multi
        if stack:
            stack[-1][-1]+=res
        else:
            ans+=res
    else:
        if stack:
            stack[-1][-1]+=char
        else:
            ans+=char
print(ans)


