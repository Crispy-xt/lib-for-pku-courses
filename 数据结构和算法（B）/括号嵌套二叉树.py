class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def build_tree(s):
    if s=='*':
        return None
    if '(' not in s:
        return Treenode(s)
    root=Treenode(s[0])
    stack=[]
    s=s[2:-1]
    id=None
    for i,char in enumerate(s):
        if char=='(':
            stack.append(char)
        elif char==')':
            stack.pop()
        elif char==',' and not stack:
            id=i
            break
    left_tree=s[:id] if id is not None else s
    right_tree=s[id+1:] if id is not None else None
    root.left=build_tree(left_tree)
    root.right=build_tree(right_tree) if right_tree else None
    return root

def preorder_traversal(root):
    if root==None:
        return ''
    return root.value+preorder_traversal(root.left)+preorder_traversal(root.right)

def inorder_traversal(root):
    if root==None:
        return ''
    return inorder_traversal(root.left)+root.value+inorder_traversal(root.right)

n = int(input())
for _ in range(n):
    s=input()
    tree=build_tree(s)
    preorder=preorder_traversal(tree)
    inorder=inorder_traversal(tree)
    print(preorder)
    print(inorder)
