def move_zeroes(arr):
    index = 0  
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1

arr = [0, 1, 0, 3, 12]
move_zeroes(arr)
print("After moving zeroes:", arr)  
