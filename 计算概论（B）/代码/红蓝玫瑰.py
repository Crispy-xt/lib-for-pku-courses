s=input()
n=len(s)
lst=[]
i=0
while i<=n-1:
    cnt=1
    while i!=n-1 and s[i+1]==s[i]:
        cnt+=1
        i+=1
    lst.append(cnt)
    i+=1

m=len(lst)
dp1=[0]
dp2=[1]
for i in range(1,m):
    if i%2:
        dp2.append(dp2[-1])
        dp1.append(min(lst[i]+dp1[-1],1+dp2[-1]))
    else:
        dp1.append(dp1[-1])
        dp2.append(min(1+dp1[-1],lst[i]+dp2[-1]))
print(dp1[-1] if s[0]=='R' else dp2[-1])