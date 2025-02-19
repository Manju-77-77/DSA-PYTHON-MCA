def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

arr = [2, 7, 11, 15]
target = 9
print("Two Sum Indices:", two_sum(arr, target))  
