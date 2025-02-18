def second_highest(numbers):
    highest = second = float('-inf')
    for num in numbers:
        if num > highest:
            second = highest
            highest = num
        elif num > second and num != highest:
            second = num
    return second if second != float('-inf') else None
numbers = [3, 1, 7, 2, 5, 9]
print("Second Highest:", second_highest(numbers))