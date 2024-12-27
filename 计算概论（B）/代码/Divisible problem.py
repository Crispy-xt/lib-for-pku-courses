def min_move(a,b):
    remain=a%b
    if remain==0:
        return 0
    else:
        return(b-remain)

n=int(input())
lst=[]
for i in range(n):
    a,b=map(int,input().split())
    lst.append(min_move(a,b))
for i in lst:
    print(i)