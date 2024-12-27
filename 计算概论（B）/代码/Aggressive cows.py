def is_ok(dist):
    cnt, start, end = 0, 0, 0
    while end < n:
        if stall[end] - stall[start] < dist:
            end += 1
        else:
            start = end
            cnt += 1
    return cnt >= c - 1


def binary_search():
    ll, rr = 1, (stall[-1] - stall[0]) // (c - 1)
    while not is_ok(rr):
        mid = (ll + rr) // 2
        if is_ok(mid):
            ll = mid
            rr -= 1
        else:
            rr = mid
    return rr


n, c = map(int, input().split())
stall = sorted(list(int(input()) for _ in range(n)))
print(binary_search())
