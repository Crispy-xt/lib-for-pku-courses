n,m=map(int,input().split())
days=n
plus=int(n/m)
remain=n%m
while plus>=1:
    days+=plus
    plus=int((plus+remain)/m)
    remain=(days)%m
print(days)