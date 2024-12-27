def pair(boys, girls):
    if len(boys) * len(girls) == 0:
        return 0
    else:
        b = min(boys)
        g = min(girls)
        if b <= g:
            if g == b or g == b + 1:
                boys.remove(b)
                girls.remove(g)
                return 1 + pair(boys, girls)
            else:
                boys.remove(b)
                return pair(boys, girls)
        elif g == b - 1:
            boys.remove(b)
            girls.remove(g)
            return 1 + pair(boys, girls)
        else:
            girls.remove(g)
            return pair(boys, girls)


n = int(input())
numbers = input()
boys = []
girls = []
boys = list(map(int, numbers.split()))
m = int(input())
numbers = input()
girls = list(map(int, numbers.split()))
print(pair(boys, girls))
