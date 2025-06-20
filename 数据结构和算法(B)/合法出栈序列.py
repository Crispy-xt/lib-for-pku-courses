def is_available_sequence(s, sequence):
    if len(s)!=len(sequence):
        return False
    stack = []
    id, i = 0, 0
    while i < len(s):
        ele = sequence[id]
        char = s[i]
        if ele in stack:
            if ele == stack[-1]:
                stack.pop()
                id += 1
            else:
                return False
        else:
            stack.append(char)
            i += 1
    if ''.join(stack[::-1]) != sequence[id:]:
        return False
    return True


s = input().strip()
while True:
    try:
        sequence = input().strip()
        print("YES") if is_available_sequence(s, sequence) else print("NO")
    except EOFError:
        break
