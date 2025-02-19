def insert_sorted(arr, element):
    index = 0
    while index < len(arr) and arr[index] < element:
        index += 1
    arr.append(0)  
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = element  