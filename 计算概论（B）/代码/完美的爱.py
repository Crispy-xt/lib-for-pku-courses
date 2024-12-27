from collections import defaultdict
n=int(input())
lst=list(map(int,input().split()))
d=defaultdict(list)
d[0].append(0)
pre_sum=[0]
for i in range(1,n+1):
    pre_sum.append(pre_sum[-1]+lst[i-1]-520)
    d[pre_sum[i]].append(i)
s=0
for ele in set(pre_sum):
    s=max(s,max(d[ele])-min(d[ele]))
print(s*520)

