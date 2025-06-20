class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(lst):
    if not lst:
        return None
    root=TreeNode(lst[0])
    num=lst[0]
    id=len(lst)
    for i in range(1,len(lst)):
        if lst[i]>num:
            id=i
            break
    left_lst=lst[1:id]
    right_lst=lst[id:]
    root.left=build_tree(left_lst)
    root.right=build_tree(right_lst)
    return root

def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left)+postorder_traversal(root.right)+[root.val]

n=int(input())
lst=list(map(int,input().split()))
root=build_tree(lst)
print(' '.join(map(str,postorder_traversal(root))))  