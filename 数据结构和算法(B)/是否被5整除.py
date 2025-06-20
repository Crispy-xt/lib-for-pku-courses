s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "1":
        break
    ans += "1"
n = 0
if len(ans) != len(s):
    for c in s[i:]:
        if c == "1":
            n = n * 2 + 1
        else:
            n = n * 2
        if n % 5 == 0:
            ans += "1"
        else:
            ans += "0"
print(ans)
