def find(x,y):
    if x==y:
        return x
    if x>y:
        return find(x//2,y)
    return find(x,y//2)
x,y=map(int,input().split())
print(find(x,y))
