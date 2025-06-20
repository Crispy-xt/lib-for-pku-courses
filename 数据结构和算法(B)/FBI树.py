class Treenode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def trans(s):
    if '1' in s:
        if '0' in s:
            return 'F'
        return 'I'
    return 'B'

def build_tree(s):
    if len(s)==1:
        return Treenode(trans(s))
    n=len(s)
    root=Treenode(trans(s))
    root.left=build_tree(s[:(n+1)//2])
    root.right=build_tree(s[(n+1)//2:])
    return root

def postorder_traversal(root):
    if root is None:
        return ''
    return postorder_traversal(root.left)+postorder_traversal(root.right)+root.val

n=int(input())
s=input()
root=build_tree(s)
print(postorder_traversal(root))

