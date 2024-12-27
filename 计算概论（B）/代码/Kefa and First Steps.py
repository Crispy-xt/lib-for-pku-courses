length=int(input())
nums=map(int,input().split())
nums_list=list(nums)
nums_list.append(0)#用来保证最后可以存储进max_
i=0
max_length=1
max_=1
while i<length:
    if nums_list[i]<=nums_list[i+1]:
        max_length+=1
        i+=1
        continue
    else:
        if max_length>max_:
            max_=max_length
            max_length=1
            i+=1
            continue
        if max_length<=max_:
            max_length=1
            i+=1
print(max_)

