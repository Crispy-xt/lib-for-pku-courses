class TreeNode():
    def __init__(self,val):
        self.val=val
        self.children=[]

def build_tree(s):
    stack=[]
    for char in s:
        if char.isalpha():
            root=TreeNode(char)
            if stack:
                stack[-1].children.append(root)
        elif char=='(':
            stack.append(root)
        elif char==')':
            root=stack.pop()
    return root

def preorder_traversal(root):
    output=[root.val]
    for child in root.children:
        output.extend(preorder_traversal(child))
    return ''.join(output)

def postorder_traversal(root):
    output=[]
    for child in root.children:
        output.extend(postorder_traversal(child))
    output.extend(root.val)
    return ''.join(output)

s=input().strip()
root=build_tree(s)
preorder=preorder_traversal(root)
postorder=postorder_traversal(root)
print(preorder+'\n'+postorder)
