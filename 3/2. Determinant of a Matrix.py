def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]
    
    det = 0
    sign = 1
    for f in range(n):
        sub_matrix = [[matrix[i][j] for j in range(n) if j != f] for i in range(1, n)]
        det += sign * matrix[0][f] * determinant(sub_matrix, n - 1)
        sign = -sign  
    
    return det

# Example
matrix = [[2, 3, 1], [4, 5, 6], [7, 8, 9]]
print("Determinant:", determinant(matrix, len(matrix)))
