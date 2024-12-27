n = int(input())
for i in range(1, n + 1):
    if i != n:
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print("\r")
    if i == n:
        for j in range(n):
            print("*", end="")
