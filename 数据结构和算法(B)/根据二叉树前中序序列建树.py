class Treenode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def buildTree(preorder,inorder):
    if not preorder:
        return None
    root=Treenode(preorder[0])
    for i in range(len(inorder)):
        if inorder[i]==root.val:
            id=i
            break
    left_preorder=preorder[1:id+1]
    right_preorder=preorder[id+1:]
    left_inorder=inorder[:id]
    right_inorder=inorder[id+1:]
    root.left=buildTree(left_preorder,left_inorder)
    root.right=buildTree(right_preorder,right_inorder)
    return root

def postorder_traversal(root):
    if root is None:
        return ''
    return postorder_traversal(root.left)+postorder_traversal(root.right)+root.val

while True:
    try:
        preorder=input()
        inorder=input()
        root=buildTree(preorder,inorder)
        print(postorder_traversal(root))
    except EOFError:
        break
