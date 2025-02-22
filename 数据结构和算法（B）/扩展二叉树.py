class TreeNode():
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None

def build_tree(lst):
    if not lst:
        return None
    node=lst.pop()
    if node=='.':
        return None
    root=TreeNode(node)
    root.left=build_tree(lst)
    root.right=build_tree(lst)
    return root
    

def inorder_traversal(root):
    if root is None:
        return ''
    return inorder_traversal(root.left)+root.val+inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return ''
    return postorder_traversal(root.left)+postorder_traversal(root.right)+root.val

lst=list(input())
lst=lst[::-1]
root=build_tree(lst)
inorder=inorder_traversal(root)
postorder=postorder_traversal(root)
print(inorder)
print(postorder)
