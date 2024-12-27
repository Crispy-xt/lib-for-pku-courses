n = int(input())
numbers = input()
lst = list(map(int, numbers.split()))
max = 0
for ele in lst:
    if lst.count(ele) > max:
        max = lst.count(ele)
print(max)
