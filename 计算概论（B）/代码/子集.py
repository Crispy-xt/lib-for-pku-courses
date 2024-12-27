def sub_set(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


nums = sorted(list(map(int, input().split())))
result = sub_set(nums)
for res in result:
    print(" ".join(map(str, res)))
