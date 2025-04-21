def get_prime():
    """Function to get prime numbers from 2 to 10^4"""
    prime = []
    lower = 2
    upper = 10000
    
    for i in range(lower, upper):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            prime.append(i)
    
    return prime

def waiter(number, q):
    result = []
    prime = get_prime()  # assign all prime numbers to array
    
    for i in range(q):
        str_a = []
        str_b = []
        
        while number:
            num = number.pop()
            
            # if the number is divisible by the prime number, store it to stack str_b
            # if not, store it to stack str_a
            if num % prime[i] == 0:
                str_b.append(num)
            else:
                str_a.append(num)
        
        number = str_a  # do the iteration with numbers in str_a
        
        # move the str_b stack values to the result stack
        while str_b:
            result.append(str_b.pop())
    
    # if the number stack is not empty after all iterations, move it to result stack
    while number:
        result.append(number.pop())
    
    return result

if __name__ == "__main__":
    n, q = map(int, input().split())
    number = list(map(int, input().split()))
    
    result = waiter(number, q)
    
    for num in result:
        print(num)
