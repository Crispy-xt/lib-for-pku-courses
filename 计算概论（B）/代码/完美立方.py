n = int(input())
for a in range(6, n + 1):
    r = a**3
    for b in range(2, a):
        s = r - b**3
        for c in range(b, a):
            t = s - c**3
            for d in range(c, a):
                if t == d**3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
