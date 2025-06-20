from collections import deque
def gcd(a,b):
    if a%b==0:
        return b
    elif b%a==0:
        return a
    else:
        return gcd(b,a%b) if a>b else gcd(a,b%a)

def bfs(a,b,c):
    if c%gcd(a,b)!=0:
        print('impossible')
    else:
        seen=set((0,0))
        q=deque([(0,0,0,'')])
        while q:
            step,x,y,word=q.popleft()
            if x==c or y==c:
                print(step)
                lst=[s for s in word.split()]
                for s in lst:
                    print(s)
                break
            if (0,y) not in seen:
                q.append((step + 1, 0, y, word + ' DROP(1)'))
                seen.add((0,y))
            if (x,0) not in seen:
                q.append((step + 1, x, 0, word + " DROP(2)"))
                seen .add((x,0))
            if (a,y) not in seen:
                q.append((step + 1, a, y, word + " FILL(1)"))
                seen.add((a,y))
            if (x,b) not in seen:
                q.append((step + 1, x, b, word + " FILL(2)"))
            if (max(0,x+y-b),min(b,x+y)) not in seen:
                q.append((step + 1, max(0,x+y-b), min(b,x+y), word + " POUR(1,2)"))
                seen.add((max(0, x + y - b), min(b, x + y)))
            if (min(a,x+y), max(0,x+y-a)) not in seen:
                q.append((step + 1, min(a,x+y), max(0,x+y-a), word + " POUR(2,1)"))
                seen.add((min(a, x + y), max(0, x + y - a)))

a,b,c=map(int,input().split())
bfs(a,b,c)
