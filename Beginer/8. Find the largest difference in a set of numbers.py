def largest_difference(numbers):
    smallest, largest = numbers[0], numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest
numbers = [3, 1, 7, 2, 5, 9]
print("Largest Difference:", largest_difference(numbers))