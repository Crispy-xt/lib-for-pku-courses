class Treenode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node,value):
    if node is None:
        return Treenode(value)
    if value<node.val:
        node.left=insert(node.left,value)
    if value>node.val:
        node.right=insert(node.right,value)
    return node

def level_traversal(root):
    level=[root]
    ans=[]
    while level:
        lst_val=[]
        next_level=[]
        for node in level:
            lst_val.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level=next_level
        ans+=lst_val
    return ' '.join(map(str,ans))
        

lst=list(map(int,input().split()))
s=set()
nums=[]
for ele in lst:
    if ele not in s:
        nums.append(ele)
    s.add(ele)
root=None
for ele in nums:
    root=insert(root,ele)
s=level_traversal(root)
print(s)



