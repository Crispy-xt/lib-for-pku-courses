from collections import defaultdict


def find_second_winner(matrix):
    m, n = len(matrix), len(matrix[0])
    s = set()
    d = defaultdict(int)
    for i in range(m):
        for j in range(n):
            d[matrix[i][j]] += 1
            s.add(matrix[i][j])
    rank = []
    for name in s:
        rank.append((d[name], name))
    rank.sort(reverse=True)
    lst = []
    score = rank[1][0]
    for i in range(1, len(rank)):
        if rank[i][0] == score:
            lst.append(rank[i][1])
    lst.sort()
    return " ".join(map(str, lst))


while True:
    m, n = map(int, input().split())
    mat = []
    if m == n == 0:
        break
    for i in range(m):
        mat.append(list(map(int, input().split())))
    print(find_second_winner(mat))
