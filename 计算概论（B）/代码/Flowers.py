M=10**9+7
ans,prefix_sum=[],[i+1 for i in range(10**5+1)]
n,k=map(int,input().split())
dp=[1]*(10**5+1)
for i in range(k,10**5+1):
    dp[i]=(dp[i-k]+dp[i-1])%M
    prefix_sum[i]=(prefix_sum[i-1]+dp[i])%M
for _ in range(n):
    a,b=map(int,input().split())
    ans.append((prefix_sum[b]-prefix_sum[a-1])%M)
for answer in ans:
    print(answer)
