def trans(s):
    return [d[s[i]] for i in range(len(s))]
def judge(s):
    a,b,c=s.split()
    n=len(a)
    if c=='even':
        if trans(a)!=trans(b):
            return False
    if c=='up':
        if -1 not in trans(b) and 1 not in trans(a):
            return False
    if c=='down':
        if -1 not in trans(a) and 1 not in trans(b):
            return False
    return True

coin=['A','B','C','D','E','F','G','H','I','J','K','L']
ans=[]
d={}
n=int(input())
for ele in coin:
    d[ele]=0
for _ in range(n):
    s1,s2,s3=input(),input(),input()
    for ele in coin:
        for t in [1,-1]:
            d[ele]=t
            if judge(s1) and judge(s2) and judge(s3):
                w='light' if t==-1 else 'heavy'
                ans.append(f"{ele} is the counterfeit coin and it is {w}.")
        d[ele]=0
for answer in ans:
    print(answer)
