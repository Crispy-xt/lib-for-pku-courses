from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(40))
print(f.cache_info())
