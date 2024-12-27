def prime_divisor(n,p):
    t=0
    while n%p==0:
        t+=1
        n=n/p
    return t

nums=int(input())
lst=[]
for i in range(0,nums):
    sample=int(input())
    v_2=prime_divisor(sample,2)
    v_3=prime_divisor(sample,3)
    pow_2=2**v_2
    pow_3=3**v_3
    if sample!=pow_2*pow_3:
        lst.append(-1)
        continue
    if v_2<=v_3:
        lst.append(2*v_3-v_2)
    else:
        lst.append(-1)
for ans in lst:
    print(ans)

