def compare(a, b):
    m = int(str(a) + str(b))
    n = int(str(b) + str(a))
    if m > n:
        return True
    else:
        return False


def number_sort(lst):
    sorted_lst = []
    while lst:
        max_value = lst[0]
        n = len(lst)
        pos = 0
        for i in range(n):
            if compare(lst[i], max_value):
                max_value = lst[i]
                pos = i
        sorted_lst.append(str(max_value))
        lst.pop(pos)
    return sorted_lst


n = int(input())
lst = list(map(int, input().split()))
sorted_lst = number_sort(lst)
sorted_lst_reverse = sorted_lst[::-1]
print("".join(sorted_lst) + " " + "".join(sorted_lst_reverse))
