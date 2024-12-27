def trans(date):
    haab = [
        "pop",
        "no",
        "zip",
        "zotz",
        "tzec",
        "xul",
        "yoxkin",
        "mol",
        "chen",
        "yax",
        "zac",
        "ceh",
        "mac",
        "kankin",
        "muan",
        "pax",
        "koyab",
        "cumhu",
        "uayet",
    ]
    tzolkin = [
        "imix",
        "ik",
        "akbal",
        "kan",
        "chicchan",
        "cimi",
        "manik",
        "lamat",
        "muluk",
        "ok",
        "chuen",
        "eb",
        "ben",
        "ix",
        "mem",
        "cib",
        "caban",
        "eznab",
        "canac",
        "ahau",
    ]
    day, date = date.split(". ")
    month, year = date.split()
    day = int(day)
    month = haab.index(month)
    year = int(year)
    d = month * 20 + year * 365 + day
    year = d // 260
    day = d % 13 + 1
    month = tzolkin[d % 20]
    return f"{day} {month} {year}"


n = int(input())
ans = []
for _ in range(n):
    date = input()
    ans.append(trans(date))
print(n, end="\n")
for answer in ans:
    print(answer)
