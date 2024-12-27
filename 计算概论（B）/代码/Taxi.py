n = int(input())
lst = list(map(int, input().split()))
taxi, a1, a2, a3 = 0, 0, 0, 0
for ele in lst:
    if ele == 4:
        taxi += 1
    if ele == 3:
        a3 += 1
    if ele == 2:
        a2 += 1
    if ele == 1:
        a1 += 1
while a3 > 0:
    taxi += 1
    a3 -= 1
    if a1 > 0:
        a1 -= 1
taxi += a2 // 2
a2 = a2 % 2
if a2 == 1:
    taxi += 1 + (a1 + 1) // 4
else:
    taxi += (a1 + 3) // 4
print(taxi)
