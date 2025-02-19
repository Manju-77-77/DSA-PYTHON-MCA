def union_of_sets(set1, set2):
    union_set = []
    for num in set1:
        if num not in union_set:
            union_set.append(num)
    for num in set2:
        if num not in union_set:
            union_set.append(num)
    return union_set