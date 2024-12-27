"""import math
rest = [0,5,3,1]

while True:
    a,b,c,d,e,f = map(int,input().split())
    if a + b + c + d + e + f == 0:
        break
    boxes = d + e + f           #装4*4, 5*5, 6*6
    boxes += math.ceil(c/4)     #填3*3
    spaceforb = 5*d + rest[c%4] #能和4*4 3*3 一起放的2*2
    if b > spaceforb:
    	boxes += math.ceil((b - spaceforb)/9)
    spacefora = boxes*36 - (36*f + 25*e + 16*d + 9*c + 4*b)     #和其他箱子一起的填的1*1
    
    if a > spacefora:
        boxes += math.ceil((a - spacefora)/36)
    print(boxes)"""

import math


def func_2(a, b):
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    n_2 = b // 9
    remain_2 = b % 9
    if remain_2 == 0:
        return n_2 + math.ceil(a / 36)
    elif a <= 36 - 4 * remain_2:
        return n_2 + 1
    else:
        return n_2 + 1 + math.ceil((a - 36 + 4 * remain_2) / 36)


def func_3(a, b, c):
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    if c < 0:
        c = 0
    n_3 = c // 4
    remain_3 = c % 4
    if remain_3 == 0:
        return n_3 + func_2(a, b)
    if remain_3 == 1:
        if b >= 6:
            b = b - 5
            a = a - 7
            return n_3 + func_2(a, b) + 1
        else:
            a = a - 27 + 4 * b
            b = 0
            return n_3 + func_2(a, b) + 1
    if remain_3 == 2:
        if b >= 4:
            b = b - 3
            a = a - 6
            return n_3 + func_2(a, b) + 1
        else:
            a = a - (18 - 4 * b)
            b = 0
            return n_3 + func_2(a, b) + 1
    if remain_3 == 3:
        if b >= 2:
            b = b - 1
            a = a - 5
            return n_3 + func_2(a, b) + 1
        else:
            a = a - (9 - 4 * b)
            b = 0
            return n_3 + func_2(a, b) + 1


def func_6(a, b, c, d, e, f):
    lst = [a, b, c, d, e, f]
    n_6 = f
    n_5 = e
    n_4 = d
    a = a - 11 * e
    if b >= 5 * d:
        b = b - 5 * d
        return n_4 + n_5 + n_6 + func_3(a, b, c)
    else:
        a = a - (20 * d - 4 * b)
        b = 0
        return n_4 + n_5 + n_6 + func_3(a, b, c)


while True:
    a, b, c, d, e, f = map(int, input().split())
    if a + b + c + d + e + f != 0:
        print(func_6(a, b, c, d, e, f))
    else:
        break
