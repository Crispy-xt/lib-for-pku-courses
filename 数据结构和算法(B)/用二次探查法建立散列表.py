import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index : index + n]]

hash_table = [None] * m
ans = []
i = 0
for num in num_list:
    p0 = p = num % m
    while hash_table[p] is not None and hash_table[p] != num: 
        delta = (i // 2 + 1) ** 2 * (-1 if i % 2 else 1)
        p = (p0 + delta) % m
        i += 1
    hash_table[p] = num
    ans.append(p)
print(" ".join(map(str, ans)))
