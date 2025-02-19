def delete_at_k(arr, k):
    if k < 0 or k >= len(arr):
        return arr  
    for i in range(k, len(arr) - 1):
        arr[i] = arr[i + 1] 
    arr.pop()  
