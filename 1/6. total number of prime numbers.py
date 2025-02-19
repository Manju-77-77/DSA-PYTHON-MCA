def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count
print("Prime Count:", count_primes(numbers))