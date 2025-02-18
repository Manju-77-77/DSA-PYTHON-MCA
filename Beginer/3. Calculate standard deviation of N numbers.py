def standard_deviation(numbers):
    sum_values = 0
    n = len(numbers)
    
 
    for num in numbers:
        sum_values += num
    mean = sum_values / n
 
    variance_sum = 0
    for num in numbers:
        variance_sum += (num - mean) ** 2
    variance = variance_sum / n
   
    std_dev = variance ** 0.5
    return std_dev