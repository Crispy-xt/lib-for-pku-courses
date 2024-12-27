def prime_set(max_):
    is_prime = [True] * (max_ + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_:
        if is_prime[p]:
            for i in range(p * p, max_ + 1, p):
                is_prime[i] = False
        p += 1
    return {num for num, prime in enumerate(is_prime) if prime}


s = int(input())
primes = prime_set(s)
for i in range(s // 2 + 1, 2, -1):
    if i in primes and s - i in primes:
        print(i * (s - i))
        break
