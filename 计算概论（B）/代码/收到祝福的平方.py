import math
def is_square(n):
    n=int(n)
    if math.sqrt(n)==int(math.sqrt(n)) and n!=0:
        return True
    else:
        return False

num=list(input())
n=len(num)
dp=[False]*(n+1)
for i in range(1,n+1):
    if is_square(int("".join(num[:i]))):
        dp[i]=True
for i in range(2,n+1):
    for j in range(1,i):
        if dp[j] and is_square(int("".join(num[j:i]))):
            dp[i]=True
            break
print("Yes" if dp[n] else "No")