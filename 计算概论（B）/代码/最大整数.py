def compare(a,b):
    x,y=a+b,b+a
    if int(x)<int(y):
        return True
    elif int(x)==int(y) and len(a)>len(b):
        return True
    return False

def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if compare(lst[i],lst[j]):
                lst[i],lst[j]=lst[j],lst[i]
    return lst

m=int(input())
n=int(input())
lst=list(map(str,input().split()))
bubble_sort(lst)
l=[]
for i in range(n):
    l.append(len(lst[i]))
dp=[["" for _ in range(m+1)] for _ in range(n)]
if l[n-1]<=m:
    for j in range(l[n-1],m+1):
        dp[n-1][j]=lst[n-1]
for i in range(n-2,-1,-1):
    for j in range(m+1):
        dp[i][j]=dp[i+1][j]
        if j>=l[i]:
            if dp[i+1][j]=="":
                dp[i][j]=lst[i]
            else:
                s=max(int(lst[i]+dp[i+1][j-l[i]]),int(dp[i+1][j]))
                s=str(s)
                dp[i][j]=s
print(dp[0][m])

