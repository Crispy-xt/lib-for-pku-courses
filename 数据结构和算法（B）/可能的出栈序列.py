def catalan_permutation(n):
    perm=[]
    path=[]
    def dfs(i,j): # path 中已经加入了i个元素，其中j个是1，即入栈
        if i==2*n:
            perm.append(path[:])
            return
        if 2*j==i:
            path.append(1)
            dfs(i+1,j+1)
            path.pop()
        elif j==n:
            path.append(0)
            dfs(i+1,j)
            path.pop()
        else:
            path.append(1)
            dfs(i + 1, j + 1)
            path.pop()
            path.append(0)
            dfs(i + 1, j)
            path.pop()
    dfs(0,0)
    return perm

n=int(input())
perm=catalan_permutation(n)
for path in perm:
    k=1
    stack=[]
    pop_lst=[]
    for op in path:
        if op==1:
            stack.append(k)
            k+=1
        else:
            pop_lst.append(stack.pop())
    print(pop_lst)

