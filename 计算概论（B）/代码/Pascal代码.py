s = input()
a, b, c = 0, 0, 0
for i in range(len(s)):
    if s[i] == "a":
        a = int(s[i + 3])
    if s[i] == "b":
        b = int(s[i + 3])
    if s[i] == "c":
        c = int(s[i + 3])
    else:
        continue
print(a, b, c)
