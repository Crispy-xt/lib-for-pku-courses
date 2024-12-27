import sys
n,m,k=map(int,input().split())
dp=[[-1 for _ in range(m+1)] for _ in range(k+1)] # dp[i][j]表示用j点体力收服i个精灵所剩下的最大球数
for i in range(1,m+1):
    dp[0][i]=n
for t in range(1,k+1):
    x,y=map(int,input().split())
    for i in range(t,-1,-1): # 避免重复
        for j in range(1,m+1):
            if j-y>0 and x<=dp[i-1][j-y]: # 可以收服
                dp[i][j]=max(dp[i][j],dp[i-1][j-y]-x)
for i in range(k,-1,-1):
    for j in range(1,m+1):
        if dp[i][j]>=0:
            print(i,m-j+1)
            sys.exit()

            

    