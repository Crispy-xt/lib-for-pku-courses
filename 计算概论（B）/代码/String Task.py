string=input()
string=string.lower()
del_=["a","o","y","e","u","i"]
lst=[char for char in string if char not in del_]
for char in lst:
    print(f".{char}",end="")

