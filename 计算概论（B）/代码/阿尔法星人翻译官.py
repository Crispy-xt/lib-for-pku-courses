def trans(s, num):
    if num in dict_1:
        s += dict_1[num]
        return s
    else:
        s *= dict_2[num]
        return s


dict_1 = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
dict_2 = {"hundred": 100, "thousand": 1000, "million": 1000000}
lst = list(input().split())
flag = True
ans = 0
if lst[0] == "negative":
    flag = False
    lst.pop(0)
if "million" in lst:
    pos = lst.index("million")
    for i in range(pos):
        ans = trans(ans, lst[i])
    ans *= 1000000
    t = 0
    for i in range(pos + 1, len(lst)):
        t = trans(t, lst[i])
        if lst[i] == "thousand":
            ans += t
            t = 0
    ans += t
else:
    t = 0
    for i in range(len(lst)):
        t = trans(t, lst[i])
        if lst[i] == "thousand":
            ans += t
            t = 0
    ans += t
if flag:
    print(ans)
else:
    print(-ans)
