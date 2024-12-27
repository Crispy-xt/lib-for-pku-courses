def find_missing_and_extra_students(n, remaining_ids):
    # 创建一个集合表示原本的小朋友编号
    original_ids = set(range(1, n + 1))
    
    # 创建集合表示剩余的小朋友编号
    remaining_set = set(remaining_ids)
    
    # 找出走丢的小朋友（在original_ids中但不在remaining_set中）
    missing_students = sorted(original_ids - remaining_set)
    
    # 找出其他班的小朋友（在remaining_set中但编号大于n）
    extra_students = sorted([student for student in remaining_set if student > n])
    
    return missing_students, extra_students

# 输入部分
n = int(input())
remaining_ids = list(map(int, input().split()))

# 处理并输出结果
missing_students, extra_students = find_missing_and_extra_students(n, remaining_ids)

# 输出走丢的小朋友
print(" ".join(map(str, missing_students)))
# 输出其他班的小朋友
print(" ".join(map(str, extra_students)))