def prime_set(max_):
    is_prime=[True]*(max_+1)
    is_prime[0]=is_prime[1]=False
    p=2
    while p*p<=max_:
        if is_prime[p]:
            for i in range(p*p,max_+1,p):
                is_prime[i]=False
        p+=1
    return {a for a, b in enumerate(is_prime) if b}        


def judge_Tprime(n,primes):
    sqrt_n=int(n**0.5)
    return sqrt_n**2==n and sqrt_n in primes

n=int(input())
numbers=input()
lst=list(map(int,numbers.split()))
max_=int(max(lst)**0.5)
primes=prime_set(max_)
for i in range(n):
    if judge_Tprime(lst[i],primes):
        print("YES")
    else:
        print("NO")