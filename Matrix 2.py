matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums = []
col_sums = [0] * 3  

for i in range(len(matrix)):
    row_sum = 0 
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]  
        col_sums[j] += matrix[i][j]  
    
    row_sums.append(row_sum)  

print("Input Array:")
for row in matrix:
    print("\t".join(map(str, row)))

print("\nSum of rows:")
print(row_sums)

print("\nSum of columns:")
print(col_sums)
