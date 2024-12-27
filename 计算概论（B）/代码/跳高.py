def binary_search(lst, n):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            right = mid - 1
        else:
            left = mid + 1
    return left


n = int(input())
height = []
current_height = [999999]
quantities = 0
height = list(map(int, input().split()))
for h in height:
    pos = binary_search(current_height, h)
    if pos == len(current_height):
        quantities += 1
        current_height.append(h)
    else:
        current_height[pos] = h

print(quantities)
