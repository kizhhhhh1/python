Mat1 = [[1, 2], [5, 3]]
Mat2 = [[2, 3], [4, 1]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += Mat1[i][k] * Mat2[k][j]

for row in result:
    print(row)
