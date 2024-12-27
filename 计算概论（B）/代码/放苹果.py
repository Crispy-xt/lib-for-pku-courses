def way(m,n):
    dp=[[[0 for _ in range(m+1)] for _ in range(m+1)] for _ in range(n+1)] # dp[i][j][k]表示i个正数之和为k，最大数为j的拆分数
    for k in range(1,m+1):
        for i in range(1,min(k,n)+1):
            for j in range((k-1)//i+1,k-i+2):
                if i==1:
                    dp[i][j][k]+=1
                else:
                    for t in range(1,j+1):
                        dp[i][j][k]+=dp[i-1][t][k-j]
    s=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            s+=dp[i][j][m]
    return s

ans=[]
for _ in range(int(input())):
    m,n=map(int,input().split())
    ans.append(way(m,n))
for answer in ans:
    print(answer)
