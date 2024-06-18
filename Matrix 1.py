matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = []

for j in range(3): 
    transposed_row = []
    for i in range(3):  
        transposed_row.append(matrix[i][j])
    transpose.append(transposed_row)

for row in transpose:
    print("\t".join(map(str, row)))