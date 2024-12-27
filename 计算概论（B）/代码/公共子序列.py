def find_max_subsequence(s1, s2):
    n, m = len(s1), len(s2)
    dp = [
        [0 for _ in range(m + 1)] for _ in range(n + 1)
    ]  # dp[i][j]表示s1到第i位，s2到第j位的最大公共子序列长
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[n][m]


if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        if line.strip():
            s1, s2 = line.split()
            print(find_max_subsequence(s1, s2))
