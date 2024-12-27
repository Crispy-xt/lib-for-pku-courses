def maximal_binary_matrix(n, k):
    if n**2 - k < 0:
        return -1
    elif n**2 - k > 0:
        cnt, t = n, 0
        while k >= 2 * cnt - 1:
            k -= 2 * cnt - 1
            cnt -= 1
            t += 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(t):
            for j in range(n):
                matrix[i][j] = matrix[j][i] = 1
        if k > 0:
            j = t + 1
            matrix[t][t] = 1
            k -= 1
            while k >= 2:
                matrix[t][j] = matrix[j][t] = 1
                k -= 2
                j += 1
            if k:
                matrix[t + 1][t + 1] = 1
    else:
        matrix = [[1 for _ in range(n)] for _ in range(n)]
    return matrix


n, k = map(int, input().split())
ans = maximal_binary_matrix(n, k)
if ans == -1:
    print(ans)
else:
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()
