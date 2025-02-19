def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    row_flag = [0] * m
    col_flag = [0] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_flag[i] = 1
                col_flag[j] = 1
    
    for i in range(m):
        for j in range(n):
            if row_flag[i] == 1 or col_flag[j] == 1:
                matrix[i][j] = 0
    
    return matrix

# Example
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print("Updated Matrix:")
for row in set_zeroes(matrix):
    print(row)
