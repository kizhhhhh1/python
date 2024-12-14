A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row_sum = [sum(row) for row in A]
column_sum = [sum(A[i][j] for i in range(len(A))) for j in range(len(A[0]))]
diagonal_sum = sum(A[i][i] for i in range(len(A)))

print("Row sums is", row_sum)
print("Column sum is", column_sum)
print("Diagonal sum is", diagonal_sum)
