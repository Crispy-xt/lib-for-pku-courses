n=int(input())
lst1=[]
lst2=[]
for i in range(n):
    s1,s2=input().split()
    s2=int(s2)
    if s2>=60:
        lst2.append((s2,s1,i))
    else:
        lst1.append((s2,s1))

lst2.sort(reverse=True)
flag=True
while flag:
    flag=False
    for i in range(len(lst2)-1):
        if lst2[i][0]==lst2[i+1][0] and lst2[i][2]>lst2[i+1][2]:
            c=lst2[i]
            lst2[i]=lst2[i+1]
            lst2[i+1]=c
            flag=True
for ele in lst2:
    print(ele[1])
for ele in lst1:
    print(ele[1])