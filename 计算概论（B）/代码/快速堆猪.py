import sys
input=sys.stdin.read
stack,min_stack,ans=[],[],[]
data=input().splitlines()
for line in data:
    if line.startswith("push"):
        _,n=line.split()
        n=int(n)
        stack.append(n)
        if not min_stack or n<=min_stack[-1]:
            min_stack.append(n)
    elif line=="pop":
        if stack:
            m=stack.pop()
            if m==min_stack[-1]:
                min_stack.pop()
    else:
        if min_stack:
            ans.append(str(min_stack[-1]))
sys.stdout.write("\n".join(ans))