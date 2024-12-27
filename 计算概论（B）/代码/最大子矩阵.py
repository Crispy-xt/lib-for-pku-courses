def find_maximum_submatrix(matrix):
    n = len(matrix)
    max_sum = float("-inf")

    def kadane(arr):
        m = len(arr)
        max_sum = float("-inf")
        current_sum = arr[0]
        for i in range(1, m):
            current_sum = max(current_sum + arr[i], arr[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

    for top in range(n):
        arr = [0] * n
        for bottom in range(top, n):
            for i in range(n):
                arr[i] = sum(matrix[i][top : bottom + 1])
            max_sum = max(max_sum, kadane(arr))
    return max_sum


n = int(input())
num = []
while len(num) < n**2:
    num.extend(map(int, input().split()))
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = num[n * i + j]
print(find_maximum_submatrix(matrix))
