'''
debug不动了
from collections import deque
import heapq
ans=[]
q=deque()
max_heap,min_heap=[],[]
num_1,num_2=0,0
for _ in range(int(input())):
    s=input().split()
    if s[0]=='add':
        m=int(s[1])
        q.append(m)
        if min_heap:
            l=-max_heap[0]
            r=min_heap[0]
            if m<l:
                if len(q)%2:
                    heapq.heappush(max_heap,-m)
                    heapq.heappush(min_heap,l)
                else:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap,-m)
            elif m>r:
                if len(q)%2:
                    heapq.heappush(min_heap,m)
                    heapq.heappush(max_heap,-r)
                else:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,m)
            else:
                if len(q)%2:
                    heapq.heappush(min_heap,m)
                    heapq.heappush(max_heap,-m)
        else:
            heapq.heappush(max_heap,-m)
            heapq.heappush(min_heap,m)
    elif s[0]=='del':
        m=q.popleft()
        l=-max_heap[0]
        r=min_heap[0]
        if l<=m<=r and not len(q)%2:
            heapq.heappop(max_heap)
            heapq.heappop(min_heap)
        elif m<=l:
            if len(q)%2:
                max_heap.remove(-m)
                heapq.heapify(max_heap)
                heapq.heappush(max_heap,-r)
            else:
                max_heap.remove(-m)
                heapq.heappop(min_heap)
        else:
            if len(q)%2:
                min_heap.remove(m)
                heapq.heapify(min_heap)
                heapq.heappush(min_heap,l)
            else:
                min_heap.remove(m)
                heapq.heappop(min_heap)
    else:
        l=-max_heap[0]
        r=min_heap[0]
        ans.append(int((l+r)/2)) if l%2==r%2 else ans.append((l+r)/2)
for answer in ans:
    print(answer)
    '''
