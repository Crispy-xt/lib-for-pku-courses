def gcd(a,b):
    if a%b==0 or b%a==0:
        return min(a,b)
    else:
        return gcd(a,a%b) if b<a else gcd(b,b%a)

a,b,c,d=map(int,input().split())
f=b*d
e=a*d+c*b
g=gcd(e,f)
e,f=e//g,f//g
print(f'{e}/{f}')