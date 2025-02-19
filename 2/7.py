def trap_rain_water(arr):
    n = len(arr)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n
    water = 0

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]

    return water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("Trapped Water:", trap_rain_water(arr))  
