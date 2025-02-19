def decimal_to_binary(n):
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary
numbers = [3, 1, 7, 2, 5, 9]
print("Binary of 10:", decimal_to_binary(10))