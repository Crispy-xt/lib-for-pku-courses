# A:65,Z:90;a:97,z:122
k = int(input())
s = input()
l = len(s)
str_1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
str_2 = list("abcdefghijklmnopqrstuvwxyz")
for i in range(l):
    if s[i] in str_1:
        pos = str_1.index(s[i])
        pos = (pos - k) % 26
        print(str_1[pos], end="")
    else:
        pos = str_2.index(s[i])
        pos = (pos - k) % 26
        print(str_2[pos], end="")
