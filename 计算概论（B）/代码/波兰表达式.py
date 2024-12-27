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
    for ele in lst[::-1]:
        if is_number(ele):
            stack.append(float(ele))
        else:
            a = stack.pop()
            b = stack.pop()
            if ele == "+":
                stack.append(a + b)
            elif ele == "-":
                stack.append(a - b)
            elif ele == "*":
                stack.append(a * b)
            elif ele == "/":
                stack.append(a / b)
    return f"{stack.pop():.6f}"


expression = input()
print(calculate_poland_expression(expression))
