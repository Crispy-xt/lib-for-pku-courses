def is_number(s):
    try:
        float(s)
        return True
    except:
        ValueError
        return False


def calculate_poland_expression(expression):
    stack = []
    lst = expression.split()
    for ele in lst:
        if is_number(ele):
            stack.append(float(ele))
        else:
            a = stack.pop()
            b = stack.pop()
            if ele == "+":
                stack.append(a + b)
            elif ele == "-":
                stack.append(b - a)
            elif ele == "*":
                stack.append(a * b)
            elif ele == "/":
                stack.append(b / a)
    return f"{stack.pop():.2f}"

for _ in range(int(input())):
    expression = input()
    print(calculate_poland_expression(expression))
