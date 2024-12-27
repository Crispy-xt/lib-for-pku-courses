n = int(input())
number = input()
lst = list(map(int, number.split()))
queue = []
lst.sort()
disappointed_person = 0
queue.append(lst[0])
for i in range(1, n):
    if sum(queue) <= lst[i]:
        queue.append(lst[i])
print(len(queue))
