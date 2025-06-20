# 单调栈解法
def removeKDigits(num, k):
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k:
        stack.pop()
        k -= 1
    return int("".join(stack))


t = int(input())
results = []
for _ in range(t):
    n, k = input().split()
    results.append(removeKDigits(n, int(k)))
for result in results:
    print(result)
    
'''胡乱解法
def min_number(n,k):
    if k==0:
        return n
    lst=[]
    while n>=10:
        lst.append(n%10)
        n=(n-n%10)//10
    lst.append(n)
    lst=lst[::-1]
    id=-1
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst = lst[:i] + lst[i+1:]
            id=i
            break
    if id==-1:
        lst=lst[:len(lst)-1]
    lst = lst[::-1]
    n = 0
    for i in range(len(lst)):
        n += lst[i] * 10**i
    return min_number(n,k-1)

ans=[]
for _ in range(int(input())):
    n,k=map(int,input().split())
    ans.append(min_number(n,k))
for answer in ans:
    print(answer)'''
