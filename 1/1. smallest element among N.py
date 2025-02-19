def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

numbers = [3, 1, 7, 2, 5, 9]
print("Smallest:", find_smallest(numbers))