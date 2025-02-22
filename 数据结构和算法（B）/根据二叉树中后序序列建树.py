class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def build_tree(inorder,postorder):
    if not postorder:
        return None
    s=postorder[-1]
    id=0
    for i in range(len(inorder)):
        if inorder[i]==s:
            id=i
            break
    left_inorder=inorder[:i]
    right_inorder=inorder[i+1:]
    left_postorder=postorder[:i]
    right_postorder=postorder[i:-1]
    root=TreeNode(s)
    root.left=build_tree(left_inorder,left_postorder)
    root.right=build_tree(right_inorder,right_postorder)
    return root

def preorder_traversal(root):
    if root is None:
        return ''
    return root.val+preorder_traversal(root.left)+preorder_traversal(root.right)

inorder=input()
postorder=input()
root=build_tree(inorder,postorder)
print(preorder_traversal(root))