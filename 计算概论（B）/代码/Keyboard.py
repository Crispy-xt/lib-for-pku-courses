s="qwertyuiopasdfghjkl;zxcvbnm,./"
lst_check=[char for char in s]
judge=input()
string_1=input()
lst_1=[char for char in string_1]
length=len(lst_1)
if judge=="L":
    for i in range(0,length):
        pos=lst_check.index(lst_1[i])
        lst_1[i]=lst_check[pos+1]
else:
    for i in range(0,length):
        pos=lst_check.index(lst_1[i])
        lst_1[i]=lst_check[pos-1]

for t in lst_1:
    print(t,end="")


