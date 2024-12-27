def permutation(nums):
    result = []
    current = []
    used = [False] * (len(nums))

    def backtrack():
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            current.append(nums[i])
            used[i] = True
            backtrack()
            current.pop()
            used[i] = False

    backtrack()
    return result


n = int(input())
nums = sorted(list(map(int, input().split())))
result = permutation(nums)
for res in result:
    print(" ".join(map(str, res)))
