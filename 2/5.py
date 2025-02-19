def min_jumps(arr):
    if len(arr) <= 1:
        return 0
    if arr[0] == 0:
        return -1  

    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, len(arr)):
        if i == len(arr) - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i

arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print("Minimum jumps:", min_jumps(arr))  
