import heapq
class Node:
    def __init__(self,weight,char):
        self.left=None
        self.right=None
        self.char=char
        self.weight=weight
    def __lt__(self,other):
        if self.weight==other.weight:
            return self.char<other.char
        return self.weight<other.weight

def buildHuffmanTree(lst):
    q=[]
    for weight,char in lst:
        heapq.heappush(q,Node(weight,char))
    while len(q)>=2:
        left=heapq.heappop(q)
        right=heapq.heappop(q)
        merged=Node(left.weight+right.weight,min(left.char,right.char))
        merged.left=left
        merged.right=right
        heapq.heappush(q,merged)
    return q[0]

def encodeHuffmanTree(root):
    codes={}
    def traversal(node,code):
        if node.left is None and node.right is None:
            codes[node.char]=code
        else:
            traversal(node.left,code+'0')
            traversal(node.right,code+'1')
    traversal(root,'')
    return codes

def decodeHuffmanTree(root,s):
    ans=''
    node=root
    for bit in s:
        if bit=='0':
            node=node.left
        else:
            node=node.right
        if node.left is None and node.right is None:
            ans+=node.char
            node=root
    return ans

lst=[]
for _ in range(int(input())):
    char,weight=input().split()
    lst.append((int(weight),char))
HuffmanTree=buildHuffmanTree(lst)
codes=encodeHuffmanTree(HuffmanTree)

while True:
    try:
        s=input()
        if s[0] in {'0','1'}:
            print(decodeHuffmanTree(HuffmanTree,s))
        else:
            print(''.join(codes[c] for c in s))
    except EOFError:
        break