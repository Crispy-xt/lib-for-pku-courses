def check(s):
    lst = [
        "7",
        "9",
        "10",
        "5",
        "8",
        "4",
        "2",
        "1",
        "6",
        "3",
        "7",
        "9",
        "10",
        "5",
        "8",
        "4",
        "2",
    ]
    sum = 0
    for i in range(17):
        sum += int(s[i]) * int(lst[i])
    a = sum % 11
    check_lst = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    if check_lst[a] == s[17]:
        return "YES"
    else:
        return "NO"


n = int(input())
ans = []
for _ in range(n):
    s = input()
    ans.append(check(s))
for answer in ans:
    print(answer)
