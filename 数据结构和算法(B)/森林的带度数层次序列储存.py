class Tree:
    def __init__(self,val):
        self.val=val
        self.children=[]

def buildTree(nodes,nums):
    id=1
    for j in range(len(nodes)):
        node=nodes[j]
        num=nums[j]
        for i in range(id,id+num):
            node.children.append(nodes[i])
        id+=num

def postorder_traversal(root):
    if root is None:
        return []
    lst=[]
    for child in root.children:
        lst+=postorder_traversal(child)
    return lst+[root.val]

ans=[]
for _ in range(int(input())):
    lst=list(input().split())
    n=len(lst)
    nodes=[Tree(lst[i]) for i in range(0,n,2)]
    nums=[int(lst[i]) for i in range(1,n,2)]
    buildTree(nodes,nums)
    root=nodes[0]
    ans+=postorder_traversal(root)
print(' '.join(ans))