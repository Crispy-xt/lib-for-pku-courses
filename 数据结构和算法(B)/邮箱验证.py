import re

pattern = r"^[^@.]+(?:\.[^@.]+)*@[^@.]+(?:\.[^@.]+)+$"

while True:
    try:
        line = input().strip()
        if re.fullmatch(pattern, line):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break

    
"""'
def is_legal(s):
    cnt1, cnt2 = 0, 0
    for i, char in enumerate(s):
        if char == "@":
            cnt1 += 1
            id1 = i
        if char == ".":
            cnt2 += 1
            id2 = i
    if cnt1 != 1 or cnt2 == 0:
        return False
    if id1 == 0 or id1 == len(s) - 1 or id2 == len(s) - 1 or s[0] == ".":
        return False
    if id2 <= id1 + 1 or s[id1 + 1] == "." or s[id1 - 1] == ".":
        return False
    return True


while True:
    try:
        email = input()
        if is_legal(email):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break'
    """
