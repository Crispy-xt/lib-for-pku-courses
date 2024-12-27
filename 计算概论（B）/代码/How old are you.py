def cal(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
n=int(input())
while n!=1:
    if n%2==0:
        print(f"{n}/2={cal(n)}")
        n=cal(n)
    else:
        print(f"{n}*3+1={cal(n)}")
        n=cal(n)