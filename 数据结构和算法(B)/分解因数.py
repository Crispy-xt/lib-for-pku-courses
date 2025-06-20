def dfs(n,k):
    global cnt
    if n==1:
        cnt+=1
        return
    for i in range(k,n+1):
        if n%i==0:
            dfs(n//i,i)

for _ in range(int(input())):
    cnt=0
    n=int(input())
    dfs(n,2)
    print(cnt)
            
