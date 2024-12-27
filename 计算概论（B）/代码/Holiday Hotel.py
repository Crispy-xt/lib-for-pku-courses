'''while True:
    n=int(input())
    if n!=0:
        dist_cost=[]
        for _ in range(n):
            d,c=map(int,input().split())
            dist_cost.append((d,c))

        dist_cost.sort()
        timer=0
        min=10000000
        for d,c in dist_cost:
            if c<min:
                timer+=1
                min=c
        print(timer)
        
    else:
        break'''


n=int(input())
if n!=0:
    dist_cost=[]
    for _ in range(n):
        d,c=map(int,input().split())
        dist_cost.append((d,c))

    dist_cost.sort()
    print(dist_cost)
