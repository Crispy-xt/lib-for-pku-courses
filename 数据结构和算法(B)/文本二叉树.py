class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root is None:
        return ""
    return postorder_traversal(root.left) + postorder_traversal(root.right) + root.val

def preorder_traversal(root):
    if root is None:
        return ""
    return root.val + preorder_traversal(root.left) + preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return ""
    return inorder_traversal(root.left) + root.val + inorder_traversal(root.right) 

n=int(input())
cnt=0
d={}
is_None={}
while cnt<n:
    s=input()
    if s=='0':
        cnt+=1
        root=d[0]
        print(preorder_traversal(root))
        print(postorder_traversal(root))
        print(inorder_traversal(root))
        print()
    else:
        char=s[-1]
        k=len(s)-1
        if k>=1:
            if char!='*':
                d[k]=Treenode(char)
                if is_None.get(d[k-1],False) or d[k-1].left is not None:
                    d[k-1].right=d[k]
                else:
                    d[k-1].left=d[k]
            else:
                is_None[d[k-1]]=True
        else:
            d[0]=Treenode(char)