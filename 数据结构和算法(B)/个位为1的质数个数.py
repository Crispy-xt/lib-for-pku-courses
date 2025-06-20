def prime_set():
    M=10000
    is_prime=[True]*10001
    is_prime[0]=is_prime[1]=False
    p=2
    while p**2<=M:
        if is_prime[p]:
            for i in range(p*p,M+1,p):
                is_prime[i]=False
        p+=1
    return {a for a,b in enumerate(is_prime) if b}

s=prime_set()
lst=[ele for ele in s if ele%10==1]
lst.sort()
n=int(input())
for i in range(1,n+1):
    sup=int(input())
    ans=[]
    for ele in lst:
        if ele>=sup:
            break
        ans.append(ele)
    print(f'Case{i}:')
    if not ans:
        print('NULL')
    else:
        print(' '.join(map(str,ans)))
