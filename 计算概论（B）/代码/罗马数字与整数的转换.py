dict_1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = input()
l = len(s)
if s[0] not in list("123456789"):
    year = 0
    i = 0
    while i <= l - 1:
        if i != l - 1 and dict_1[s[i]] < dict_1[s[i + 1]]:
            year += dict_1[s[i + 1]] - dict_1[s[i]]
            i += 2
        else:
            year += dict_1[s[i]]
            i += 1
    print(year)
else:
    s = int(s)
    lst = []
    n1 = s // 1000
    s = s % 1000
    for _ in range(n1):
        lst.append("M")
    if s < 400:
        n2 = s // 100
        s = s % 100
        for _ in range(n2):
            lst.append("C")
    elif s < 500:
        s = s - 400
        lst.append("CD")
    elif s < 900:
        s = s - 500
        lst.append("D")
        n2 = s // 100
        s = s % 100
        for _ in range(n2):
            lst.append("C")
    else:
        s = s - 900
        lst.append("CM")

    if s < 40:
        n2 = s // 10
        s = s % 10
        for _ in range(n2):
            lst.append("X")
    elif s < 50:
        s = s - 40
        lst.append("XL")
    elif s < 90:
        s = s - 50
        lst.append("L")
        n2 = s // 10
        s = s % 10
        for _ in range(n2):
            lst.append("X")
    else:
        s = s - 90
        lst.append("XC")

    if s < 4:
        n2 = s
        for _ in range(n2):
            lst.append("I")
    elif s < 5:
        lst.append("IV")
    elif s < 9:
        s = s - 5
        lst.append("V")
        n2 = s
        for _ in range(n2):
            lst.append("I")
    else:
        lst.append("IX")
    print("".join(lst))
