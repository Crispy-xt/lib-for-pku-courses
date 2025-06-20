n, k = map(int, input().split())
nums = []
for i in range(n):
    a, b = map(int, input().split())
    nums.append((a, b, i))
nums.sort(reverse=True)
nums = nums[:k]
vote = []
for a, b, i in nums:
    vote.append((b, i))
vote.sort(reverse=True)
print(vote[0][-1] + 1)
