class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n = int(input())
lst = list(map(int, input().split()))
nodes = [Treenode(lst[i]) for i in range(n)]
for i in range(n):
    if 2 * i + 1 < n:
        nodes[i].left = nodes[2 * i + 1]
    if 2 * i + 2 < n:
        nodes[i].right = nodes[2 * i + 2]


def find_max_value(root):
    if root is None:
        return 0
    a = find_max_value(root.left) + find_max_value(root.right)
    b = root.val
    if root.left:
        b += find_max_value(root.left.left) + find_max_value(root.left.right)
    if root.right:
        b += find_max_value(root.right.left) + find_max_value(root.right.right)
    return max(a, b)


root = nodes[0]
print(find_max_value(root))
