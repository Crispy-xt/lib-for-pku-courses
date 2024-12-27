n=int(input())
numbers=input()
lst=list(map(int,numbers.split()))
m=int(input())
times=0
for i in range(n):
    if m-lst[i] in lst:
        times+=1
print(times//2)