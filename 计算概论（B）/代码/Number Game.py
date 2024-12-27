def maximal_game_round(lst):
    n = max(max(lst), len(lst))
    count_lst = [0] * (n + 1)
    for i in range(len(lst)):
        count_lst[lst[i]] += 1
    presum_lst = [0] * (n + 1)
    for i in range(1, n + 1):
        presum_lst[i] = presum_lst[i - 1] + count_lst[i]
    for i in range(1, n + 1):
        presum_lst[i] -= i - 1  # 在presum_lst中找最大的k使得1到k的索引上的数都大于等于k
    m, maximal_round = presum_lst[1], 0
    for ele in range(m, 0, -1):
        if min(presum_lst[1 : ele + 1]) >= ele:
            maximal_round = ele
            break
    return maximal_round


answer = []
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    answer.append(maximal_game_round(lst))
for ans in answer:
    print(ans)
