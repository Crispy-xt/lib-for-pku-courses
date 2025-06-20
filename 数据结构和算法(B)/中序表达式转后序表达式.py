def split_expression(string):
    separators=['(',')','+','-','*','/']
    result=[]
    num=''
    for char in string:
        if char in separators:
            if num:
                result.append(num)
                num=''
            result.append(char)
        else:
            num+=char
    if num:
        result.append(num)
    return result                


def transform(string):
    result=[]
    string=split_expression(string)
    priority={'(':1,')':1,'*':3,'/':3,'+':2,'-':2}
    operator = ["(", ")", "+", "-", "*", "/"]
    opstack=[]
    for char in string:
        if char in operator:
            if char=='(':
                opstack.append(char)
            elif char==')':
                while opstack[-1]!='(': # 此时要把括号内的所有运算符全部输出后再继续操作
                    result.append(opstack.pop())
                opstack.pop()
            else:
                while opstack and priority[char]<=priority[opstack[-1]]: # 弹出栈顶优先级更高的运算符
                    result.append(opstack.pop())
                opstack.append(char)
        else:
            result.append(char)
    while opstack:
        result.append(opstack.pop())
    return result

n=int(input())
lst=[]
for _ in range(n):
    lst.append(input())
for expression in lst:    
    print(' '.join(transform(expression)))