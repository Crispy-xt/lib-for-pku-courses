str_=input()
lst=[]
l=len(str_)
pre_sum=[]
pre_sum.append(0)
for i in range(0,l-1):
    if str_[i]==str_[i+1]:
        pre_sum.append(pre_sum[-1]+1)
    else:
        pre_sum.append(pre_sum[-1])

ans=[]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    ans.append(pre_sum[b-1]-pre_sum[a-1])

for answer in ans:
    print(answer)