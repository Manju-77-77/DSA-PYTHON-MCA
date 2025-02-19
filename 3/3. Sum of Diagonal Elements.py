def sum_of_diagonal(matrix, n):
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

matrix = [[2, 3, 1], [4, 5, 6], [7, 8, 9]]
print("Sum of Diagonal Elements:", sum_of_diagonal(matrix, len(matrix)))
