n = int(input())
lst = list(map(int, input().split()))
number_list = []
for i in range(n):
    number_list.append((lst[i], i))
number_list.sort()
for i in range(n):
    print(number_list[i][1] + 1, end=" ")
print()
s = 0
for i in range(n):
    s += number_list[i][0] * (n - i - 1)
s /= n
print("{:.2f}".format(s))
