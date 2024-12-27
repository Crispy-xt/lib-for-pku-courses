while True:
    try:
        n=int(input())
        lst=list(map(int,input().split()))
        m=max(lst)
        s=sum(lst)
        if m>=s/2:
            ans=s-m
        else:
            ans=s/2
        print(f'{ans:.1f}')
    except EOFError:
        break