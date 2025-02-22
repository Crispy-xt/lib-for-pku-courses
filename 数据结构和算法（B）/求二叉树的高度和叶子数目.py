class TreeNode:
    def __init__(self):
        self.left=None
        self.right=None

def tree_height(node):
    if not node:
        return -1
    return max(tree_height(node.left),tree_height(node.right))+1

def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left)+count_leaves(node.right)

n=int(input())
nodes=[TreeNode() for _ in range(n)]
parents=[False for _ in range(n)]
for i in range(n):
    l,r=map(int,input().split())
    if l!=-1:
        nodes[i].left=nodes[l]
        parents[l]=True
    if r!=-1:
        nodes[i].right=nodes[r]
        parents[r]=True

root=parents.index(False)
height=tree_height(nodes[root])
leaves=count_leaves(nodes[root])
print(height,leaves)