def is_ok(
    placed, row
):  # 第i+1行放置的皇后位置为placed[i]+1,判断是否能在col+1行row+1列放置皇后
    col = len(placed)
    for i in range(col):
        if placed[i] == row or placed[i] == col + row - i or placed[i] == row - col + i:
            return False
    return True


def queen(placed):
    if len(placed) == 8:
        ans.append("".join(str(placed[i] + 1) for i in range(8)))
        return

    for row in range(8):
        if is_ok(placed, row):
            placed.append(row)
            queen(placed)
            placed.pop()


ans, lst = [], []
queen([])
n = int(input())
for _ in range(n):
    pos = int(input())
    lst.append(pos)
for pos in lst:
    print(ans[pos - 1])


"""def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] == col + row - i or board[i] == col - row + i:
            return False
    return True


def find_n_queens(n, row=0, board=[]):
    if row == n:
        result.append("".join(str(board[i] + 1) for i in range(n)))
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            find_n_queens(n, row + 1, board)
            board.pop()


result = []
lst = []
find_n_queens(8)
n = int(input())
for _ in range(n):
    pos = int(input())
    lst.append(pos)
for pos in lst:
    print(result[pos - 1])"""
