def trans_1(coordinate):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    row, column = coordinate[1:].split("C")
    column = int(column)
    letters = ""
    while column > 0:
        column -= 1
        letters = alphabet[column % 26] + letters
        column //= 26
    return letters + row


def trans_2(coordinate):
    for i in range(len(coordinate)):
        if coordinate[i].isdigit():
            letters = coordinate[:i]
            row = coordinate[i:]
            break
    n = len(letters)
    column = 0
    for i in range(n):
        column += (ord(letters[i]) - 64) * (26 ** (n - i - 1))
    return f"R{row}C{column}"


n = int(input())
ans = []
for i in range(n):
    coordinate = input()
    if coordinate[0] == "R" and coordinate[1].isdigit() and "C" in coordinate:
        ans.append(trans_1(coordinate))
    else:
        ans.append(trans_2(coordinate))
print("\n".join(ans))
