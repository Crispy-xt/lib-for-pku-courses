def move(x, y):
    print(f"{x}->{y}")


def move_hannuo(n, x, y, z):
    if n == 1:
        return move(x, z)
    else:
        move_hannuo(n - 1, x, z, y)
        move(x, z)
        move_hannuo(n - 1, y, x, z)


n = int(input())
print(2**n - 1)
move_hannuo(n, "A", "B", "C")
