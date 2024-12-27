def v_p(n, p):
    cnt = 0
    while n % p == 0:
        n //= p
        cnt += 1
    return cnt


def is_ok(m, n):
    m_2, m_3, n_2, n_3 = v_p(m, 2), v_p(m, 3), v_p(n, 2), v_p(n, 3)
    minus_2, minus_3 = n_2 - m_2, m_3 - n_3
    if (
        minus_2 >= 0
        and minus_3 >= 0
        and minus_3 >= minus_2
        and n / m == (2**minus_2) / (3**minus_3)
    ):
        return True
    return False


ans = []
for _ in range(int(input())):
    m, n = map(int, input().split())
    if is_ok(m, n):
        ans.append("YES")
    else:
        ans.append("NO")
for answer in ans:
    print(answer)
