import sys


def build_next(pattern):
    n = len(pattern)
    next_array = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = next_array[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        next_array[i] = j
    return next_array


def main():
    test_case = 1
    while True:
        n_line = sys.stdin.readline()
        if not n_line:
            break
        n = int(n_line.strip())
        if n == 0:
            break
        s = sys.stdin.readline().strip()
        next_array = build_next(s)
        print(f"Test case #{test_case}")
        for i in range(2, n + 1):
            len_val = next_array[i - 1]
            if len_val == 0:
                continue
            d = i - len_val
            if i % d == 0:
                print(f"{i} {i // d}")
        print()  
        test_case += 1


if __name__ == "__main__":
    main()
