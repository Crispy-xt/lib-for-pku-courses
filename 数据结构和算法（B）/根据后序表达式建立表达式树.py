class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree(s):
    stack=[]
    for char in s:
        if 97<=ord(char)<=122:
            stack.append(TreeNode(char))
        else:
            right_node=stack.pop()
            left_node=stack.pop()
            root=TreeNode(char)
            root.left=left_node
            root.right=right_node
            stack.append(root)
    return root

def level_order(root):
    if root is None:
        return ''
    answer=''
    level=[root]
    while level:
        level_val=[]
        next_level=[]
        for node in level:
            level_val.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        answer+=''.join(level_val)
        level=next_level
    return answer

n=int(input())
ans=[]
for _ in range(n):
    s=input()
    root=build_tree(s)
    answer=level_order(root)
    ans.append(answer[::-1])
for answer in ans:
    print(answer)
        

