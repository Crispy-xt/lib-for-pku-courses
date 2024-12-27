def cal(A, B, s):
    timer = 0
    for i in range(len(A)):
        if s - A[i] in B:
            for j in range(len(B)):
                if A[i] + B[j] == s:
                    timer += 1
    return timer


n = int(input())
for _ in range(n):
    A = []
    B = []
    s = int(input())
    a = int(input())
    number = input()
    A = list(map(int, number.split()))
    b = int(input())
    number = input()
    B = list(map(int, number.split()))
    print(cal(A, B, s))
