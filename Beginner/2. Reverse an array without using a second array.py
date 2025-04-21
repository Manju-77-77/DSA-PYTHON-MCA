def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i] 

numbers = [3, 1, 7, 2, 5, 9]
reverse_array(numbers)