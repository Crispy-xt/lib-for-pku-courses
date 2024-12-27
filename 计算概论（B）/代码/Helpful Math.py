string_1=input()
lst=[char for char in string_1]
length=len(lst)
num_lst=[]
for i in range(0,length,2):
    num_lst.append(lst[i])
num_lst.sort()
print(num_lst[0],end="")
for i in range(1,len(num_lst)):
    print(f"+{num_lst[i]}",end="")