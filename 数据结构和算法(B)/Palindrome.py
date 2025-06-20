n=int(input())
s=input()
prev_1=[0]*n
prev_2=[0]*n
for length in range(2,n+1):
    cur=[]
    for i in range(n-length+1):
        j=i+length-1
        if s[i]==s[j]:
            cur.append(prev_1[i+1])
        else:
            cur.append(min(prev_2[i],prev_2[i+1])+1)
        prev_1[i]=prev_2[i]
        prev_2[i]=cur[i]
print(cur[0])
