from collections import defaultdict
def imformation(s):
    return (-ord(s[-1]),float(s[:-1]))

d=defaultdict(list)
name_list=[]
s=set()
for _ in range(int(input())):
    name,parameter=input().split('-')
    if name not in s:
        name_list.append(name)
    s.add(name)
    d[name].append(parameter)

name_list.sort()
for name in name_list:
    d[name]=sorted(d[name],key=imformation)
for name in name_list:
    print(name,end=': ')
    print(', '.join(d[name]))

