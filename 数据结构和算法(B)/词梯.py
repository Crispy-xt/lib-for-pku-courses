from collections import deque
from collections import defaultdict

graph = defaultdict(list)
pattern_map = defaultdict(list)
all_words = [input().strip() for _ in range(int(input()))]
visited = {word: False for word in all_words}

for word in all_words:
    for i in range(4):
        pattern = word[:i] + "*" + word[i + 1 :]
        pattern_map[pattern].append(word)

for word in all_words:
    for i in range(4):
        pattern = word[:i] + "*" + word[i + 1 :]
        for neighbor in pattern_map[pattern]:
            if neighbor != word and neighbor not in graph[word]:
                graph[word].append(neighbor)

q = deque([])
start, end = input().split()
q.append([start])
visited[start] = True
found = False
while q:
    path = q.popleft()
    vertex = path[-1]
    if vertex == end:
        print(" ".join(path))
        found = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            q.append(path + [neighbor])
if not found:
    print("NO")
