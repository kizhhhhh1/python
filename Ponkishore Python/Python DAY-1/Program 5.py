Matrix = [[4, 6, 7, 8], [3, 7, 2, 6], [7, 3, 7, 5]]

transpose = [[Matrix[j][i] for j in range(len(Matrix))] for i in range(len(Matrix[0]))]

for row in transpose:
    print(row)
