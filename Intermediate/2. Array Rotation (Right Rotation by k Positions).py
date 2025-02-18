def rotate_right(arr, k):
    n = len(arr)
    k = k % n 
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1): 
            arr[i] = arr[i-1]
        arr[0] = last

arr = [1, 2, 3, 4, 5]
rotate_right(arr, 2)
print("After rotation:", arr)  
