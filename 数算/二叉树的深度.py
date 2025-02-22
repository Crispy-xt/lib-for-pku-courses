class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def depth(root):
    if root is None:
        return 0
    l=depth(root.left)
    r=depth(root.right)
    return max(l,r)+1

n=int(input())
parent={i : False for i in range(-1,n+1)}
nodes=[TreeNode(i) for i in range(n+1)]
for i in range(1,n+1):
    left_node,right_node=map(int,input().split())
    root=nodes[i]
    root.left=nodes[left_node] if left_node!=-1 else None
    root.right=nodes[right_node] if right_node!=-1 else None
    parent[left_node]=True
    parent[right_node]=True
for i in range(1,n+1):
    if not parent[i]:
        root=nodes[i]
        break
d=depth(root)
print(d)