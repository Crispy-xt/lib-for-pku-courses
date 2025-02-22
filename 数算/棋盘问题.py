def backtrack(m):
    global cnt
    if len(path)==k:
        cnt+=1
        return
    if len(path)+n-m<k:
        return
    for row in range(m,n):
        for col in range(n):
            if board[row][col]=='#' and not placed[col]:
                path.append(col)
                placed[col]=True
                backtrack(row+1)
                col=path.pop()
                placed[col]=False

ans=[] 
while True:
    n,k=map(int,input().split())
    if n==k==-1:
        break
    board=[]
    for _ in range(n):
        board.append(list(input()))
    path=[]
    cnt=0
    placed=[False for _ in range(n)]
    backtrack(0)
    ans.append(cnt)
for answer in ans:
    print(answer)
