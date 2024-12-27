n=int(input())
sum_1=sum_2=sum_3=0
for i in range(0,n):
    a,b,c=map(int,input().split())
    sum_1+=a
    sum_2+=b
    sum_3+=c
if sum_1==sum_2==sum_3==0:
    print(f"YES")
else:
    print(f"NO")