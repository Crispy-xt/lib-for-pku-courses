s=input()
n=len(s)
lst=[]
i=0
while 2**i<=n:
    lst.append(s[2**i-1])
    i+=1
lst_reverse=lst[::-1]
ans=[]
j=0
while len(ans)<i:
    ans.append(lst[j])
    if len(ans)<i:
        ans.append(lst_reverse[j])
    j+=1
print("".join(ans))

