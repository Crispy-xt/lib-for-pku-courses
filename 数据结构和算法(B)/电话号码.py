class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.is_end_of_word=True
    
    def start_with(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return True

for _ in range(int(input())):
    n=int(input())
    nums=[]
    for _ in range(n):
        nums.append(input())
    nums.sort(reverse=True)
    trie=Trie()
    found=False
    for num in nums:
        if trie.start_with(num):
            found=True
            break
        trie.insert(num)
    if found:
        print('NO')
    else:
        print('YES')