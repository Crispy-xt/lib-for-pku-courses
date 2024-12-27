def merge(a, b):
    c = []
    i, j, cnt = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            cnt += len(a) - i
    c.extend(a[i:])
    c.extend(b[j:])
    
    return c, cnt


def merge_sort(lst, ll, rr):
    l_cnt, r_cnt = 0, 0
    if rr - ll <= 1:
        return 0
    mid = (ll + rr) // 2
    l_cnt = merge_sort(lst, ll, mid)
    r_cnt = merge_sort(lst, mid, rr)
    lst[ll:rr], merge_cnt = merge(lst[ll:mid], lst[mid:rr])
    return l_cnt + merge_cnt + r_cnt


cnt = 0
n = int(input())
lst = list(map(int, input().split()))
cnt = merge_sort(lst, 0, n)
print(cnt)
