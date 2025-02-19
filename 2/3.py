def product_except_self(arr):
    n = len(arr)
    left_products = [1] * n
    right_products = [1] * n
    output = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * arr[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * arr[i + 1]

    for i in range(n):
        output[i] = left_products[i] * right_products[i]

    return output

arr = [1, 2, 3, 4]
print("Product except self:", product_except_self(arr))  
