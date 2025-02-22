class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(leaves):
    def insert_node(root,leaf):
        if leaf<root.val:
            if root.left is None:
                root.left=TreeNode(leaf)
            else:
                insert_node(root.left,leaf)
        else:
            if root.right is None:
                root.right=TreeNode(leaf)
            else:
                insert_node(root.right,leaf)
    if not leaves:
        return None
    root=TreeNode(leaves[0])
    for leaf in leaves[1:]:
        insert_node(root,leaf)
    return root

def preorder_traversal(root):
    if root is None:
        return ""
    return root.val + preorder_traversal(root.left) + preorder_traversal(root.right)

flag=False
while True:
    leaves=[]
    while True:
        line=input().strip()
        if line=='*':
            break
        elif line=='$':
            flag=True
            break
        else:
            leaves.extend(line)
    root=build_tree(leaves[::-1])
    print(preorder_traversal(root))
    if flag:
        break


