import sys


def lucky(m):
    lst=[char for char in str(m)]
    for char in lst:
        if char!="4" and char!="7":
            return False
    return True

def division(m):
    lst=[]
    for i in range(1,int(m**0.5)+1):
        if m%i==0:
            lst.append(i)
            lst.append(m//i)
    return lst

m=int(input())
for i in division(m):
    if lucky(i):
        print("YES")
        sys.exit()
print("NO")
